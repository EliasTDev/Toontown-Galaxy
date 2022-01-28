#import Pyro.core
#import Pyro.naming
#import Pyro.errors
import sys
import datetime

import MySQLdb.constants.CR
import MySQLdb

from otp.switchboard.sbLog import sbLog
import otp.switchboard.sbConfig as sbConfig
import otp.switchboard.sbSQL as sbSQL

SERVER_GONE_ERROR = MySQLdb.constants.CR.SERVER_GONE_ERROR
SERVER_LOST = MySQLdb.constants.CR.SERVER_LOST


class sbMaildb:
    def __init__(self, log, host, port, user, passwd, db):
        self.sqlAvailable = True
        self.log = log
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbname = db
        try:
            self.db = MySQLdb.connect(host=host,
                                      port=port,
                                      user=user,
                                      password=passwd,
                                      db=db)
        except MySQLdb.OperationalError as e:
            self.log.warning(
                "Failed to connect to MySQL at %s:%d.  sbMaildb is disabled." %
                (host, port))
            self.log.warning(f"Error detail: {str(e)}")
            self.sqlAvailable = False
            return

        self.log.info("Connected to maildb at %s:%d." % (host, port))

        try:
            cursor = self.db.cursor()
            cursor.execute(f"USE `{self.dbname}`")
            self.log.debug(f"Using database '{self.dbname}'")
        except BaseException:
            self.log.debug(
                f"{self.dbname} database not found, maildb not active.")
            self.sqlAvailable = False

    def reconnect(self):
        self.log.debug("MySQL server was missing, attempting to reconnect.")
        try:
            self.db.close()
        except BaseException:
            pass
        self.db = MySQLdb.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.passwd)
        cursor = self.db.cursor()
        cursor.execute(f"USE `{self.dbname}`")
        self.log.debug(
            "Reconnected to MySQL server at %s:%d." %
            (self.host, self.port))

    def disconnect(self):
        if not self.sqlAvailable:
            return
        self.db.close()
        self.db = None

    def getMail(self, recipientId, isRetry=False):
        if not self.sqlAvailable:
            self.log.debug("sqlAvailable was false when calling getMail")
            return ()

        cursor = MySQLdb.cursors.DictCursor(self.db)
        try:
            cursor.execute(f"USE `{self.dbname}`")
            cursor.execute(sbSQL.getMailSELECT, (recipientId,))
            res = cursor.fetchallDict()
            #self.log.debug("Select was successful in sbMaildb, returning %s" % str(res))
            return res

        except MySQLdb.OperationalError as e:
            if isRetry:
                self.log.error(
                    f"Error on getMail retry, giving up:\n{str(e)}")
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getMail(recipientId, True)
            else:
                self.log.error(
                    f"Unknown error in getMail, retrying:\n{str(e)}")
                self.reconnect()
                return self.getMail(recipientId, True)
        except Exception as e:
            self.log.error(f"Unknown error in getMail, giving up:\n{str(e)}")
            return ()

    def putMail(self, recipientId, senderId, message, isRetry=False):
        if not self.sqlAvailable:
            return

        countcursor = self.db.cursor()

        try:
            countcursor.execute(f"USE `{self.dbname}`")
            countcursor.execute(sbSQL.getMailSELECT, (recipientId,))
            if countcursor.rowcount >= sbConfig.mailStoreMessageLimit:
                self.log.debug(
                    "%d's mailbox is full!  Can't fit message from %d." %
                    (recipientId, senderId))
                return

            cursor = MySQLdb.cursors.DictCursor(self.db)

            cursor.execute(sbSQL.putMailINSERT,
                           (recipientId, senderId, message))
            self.db.commit()

        except MySQLdb.OperationalError as e:
            if isRetry:
                self.log.error(
                    f"Error on putMail retry, giving up:\n{str(e)}")
                return
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                self.putMail(recipientId, senderId, message, True)
            else:
                self.log.error(
                    f"Unknown error in putMail, retrying:\n{str(e)}")
                self.reconnect()
                self.putMail(recipientId, senderId, message, True)
        except Exception as e:
            self.log.error(f"Unknown error in putMail, giving up:\n{str(e)}")
            return

    def deleteMail(self, accountId, messageId, isRetry=False):
        if not self.sqlAvailable:
            return

        cursor = MySQLdb.cursors.DictCursor(self.db)

        try:
            cursor.execute(f"USE `{self.dbname}`")
            cursor.execute(sbSQL.deleteMailDELETE, (messageId, accountId))

            if cursor.rowcount < 1:
                self.log.security(
                    "%d tried to delete message %d which didn't exist or wasn't his!" %
                    (accountId, messageId))

            self.db.commit()

        except MySQLdb.OperationalError as e:
            if isRetry:
                self.log.error(
                    f"Error in deleteMail retry, giving up:\n{str(e)}")
                return
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                self.deleteMail(accountId, messageId, True)
            else:
                self.log.error(
                    f"Unnown error in deleteMail, retrying:\n{str(e)}")
                self.reconnect()
                self.deleteMail(accountId, messageId, True)
        except Exception as e:
            self.log.error(
                f"Unknown error in deleteMail, giving up:\n{str(e)}")
            return

    def dumpMailTable(self):
        cursor = MySQLdb.cursors.DictCursor(self.db)
        cursor.execute(f"USE `{self.dbname}`")
        cursor.execute("SELECT * FROM recipientmail")
        return cursor.fetchallDict()
