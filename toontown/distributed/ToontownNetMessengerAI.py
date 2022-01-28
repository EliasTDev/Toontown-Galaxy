"""
Author: Toontown Stride
"""
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
import pickle
import zlib


class ToontownNetMessengerAI:
    """
    This works very much like the NetMessenger class except that
    this is much simpler and makes much more sense.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'ToontownNetMessengerAI')

    def __init__(self, air, msgChannel=40000, msgType=54321):
        self.air = air
        self.air.registerForChannel(msgChannel)
        self.msgChannel = msgChannel
        self.msgType = msgType

    def prepare(self, message, sentArgs=[]):
        dg = PyDatagram()
        dg.addServerHeader(self.msgChannel, self.air.ourChannel, self.msgType)
        dg.addString(message)
        dg.addString(zlib.compress(pickle.dumps(sentArgs)))
        return dg

    def send(self, message, sentArgs=[]):
        self.notify.debug(f'sendNetEvent: {message} {sentArgs!r}')
        dg = self.prepare(message, sentArgs)
        self.air.send(dg)

    def handle(self, msgType, di):
        message = di.getString()
        data = zlib.decompress(di.getString())
        sentArgs = pickle.loads(data)
        messenger.send(message, sentArgs)
