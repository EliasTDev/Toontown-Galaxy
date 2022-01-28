import builtins, os

class game:
    name = 'uberDog'
    process = 'server'

builtins.game = game

from panda3d.core import *

loadPrcFile('etc/Configrc.prc')

localPrc = 'etc/local.prc'

if os.path.exists(localPrc):
    loadPrcFile(localPrc)

from otp.uberdog.UberDogGlobal import *
from toontown.uberdog.ToontownUDRepository import ToontownUDRepository

udConfig = ''
udConfig += 'air-base-channel %s\n' % 1000000
udConfig += 'air-channel-allocation %s\n' % 999999
udConfig += 'air-stateserver %s\n' % 4002
udConfig += 'air-connect %s\n' % '127.0.0.1:7100'
udConfig += 'eventlog-host %s\n' % '127.0.0.1:7197'
loadPrcFileData('UberDOG Config', udConfig)

uber.air = ToontownUDRepository(config.GetInt('air-base-channel', 1000000), config.GetInt('air-stateserver', 4002))

host = config.GetString('air-connect', '127.0.0.1:7100')
port = 7100
if ':' in host:
    host, port = host.split(':', 1)
    port = int(port)

simbase.air.connect(host, port)

try:
    run()
except SystemExit:
    raise
except Exception:
    from otp.otpbase import PythonUtil
    from raven import Client 

    info = PythonUtil.describeException()
    import getpass
    sentryReporter = Client('https://b747c8225f394bafbdf9f830caaa293a@o1128902.ingest.sentry.io/6172162')
    sentryReporter.user_context({
        'district_name': os.getenv('DISTRICT_NAME', "NULL"),
        'SENDER_AVID': simbase.air.getAvatarIdFromSender(), 
        'SENDER_ACCOUNT_ID': simbase.air.getAccountIdFromSender(), 
        'HOST_NAME': getpass.getuser()
    })
    sentryReporter.captureMessage(info)
    print(info)
    raise
