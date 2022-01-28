import MySQLdb
import direct
from pandac.PandaModules import *

config = getConfigShowbase()

username = config.GetString("mysql-user")
password = config.GetString("mysql-passwd")
dbSalt = config.GetString("dev-branch-flavor", "")
if dbSalt:
    dbSalt = dbSalt + '_'
    pass

if username == "" or password == "":
    print("Username or password not found, check your config.prc!")
    sys.exit(2)


db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=username,
                     password=password)

print("Connected to MySQL at localhost.")

cursor = db.cursor()


def dropdb(dbname):
    try:
        print(f"Dropping database {dbname}:")
        cursor.execute(f"DROP DATABASE {dbname}")
        print("  Success!")
    except Exception as e:
        print(f"  Failed: {e}")


dropdb(f"{dbSalt}avatar_accessories")
dropdb(f"{dbSalt}avatar_friends")
dropdb(f"{dbSalt}avatars")
dropdb(f"{dbSalt}awards")
dropdb(f"{dbSalt}code_redemption")
dropdb(f"{dbSalt}guilds")
dropdb(f"{dbSalt}holidayschedules")
dropdb(f"{dbSalt}status")

db.commit()
