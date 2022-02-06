import builtins, os
import sentry_sdk
class game:
    name = 'toontown'
    process = 'server'

builtins.game = game

from panda3d.core import *

loadPrcFile('etc/Configrc.prc')

localPrc = 'etc/local.prc'

if os.path.exists(localPrc):
    loadPrcFile(localPrc)

from otp.ai.AIBaseGlobal import *
from toontown.ai.ToontownAIRepository import ToontownAIRepository
from otp.otpbase import PythonUtil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--base-channel', help='The base channel that the server may use.')
parser.add_argument('--max-channels', help='The number of channels the server may use.')
parser.add_argument('--stateserver', help="The control channel of this AI's designated State Server.")
parser.add_argument('--district-name', help="What this AI Server's district will be named.")
parser.add_argument('--astron-ip', help="The IP address of the Astron Message Director to connect to.")
parser.add_argument('--eventlogger-ip', help="The IP address of the Astron Event Logger to log to.")
args = parser.parse_args()
localconfig = ''
if args.base_channel: localconfig += 'air-base-channel %s\n' % args.base_channel
if args.max_channels: localconfig += 'air-channel-allocation %s\n' % args.max_channels
if args.stateserver: localconfig += 'air-stateserver %s\n' % args.stateserver
if args.district_name: localconfig += 'district-name %s\n' % args.district_name
if args.astron_ip: localconfig += 'air-connect %s\n' % args.astron_ip
if args.eventlogger_ip: localconfig += 'eventlog-host %s\n' % args.eventlogger_ip
loadPrcFileData('Command-line', localconfig)
simbase.air = ToontownAIRepository(config.GetInt('air-base-channel', 1000000), config.GetInt('air-stateserver', 4002), config.GetString('district-name', 'Toon Valley'))

host = config.GetString('air-connect', '127.0.0.1:7100')
port = 7100
wantSentry = ConfigVariableBool('want-Sentry', False)
if ':' in host:
    host, port = host.split(':', 1)
    port = int(port)

simbase.air.connect(host, port)


try:
    run()
except (SystemExit, KeyboardInterrupt):
    raise
except Exception as e:
    from otp.otpbase import PythonUtil

    info = PythonUtil.describeException()
    try:
        simbase.air.writeServerEvent('ai-exception', avId=simbase.air.getAvatarIdFromSender(), accId=simbase.air.getAccountIdFromSender(), exception=info)
    except AssertionError:
        print('Failed to get sender for ai exception')
    with open(config.GetString('ai-crash-log-name', 'ai-crash.txt'), 'w+') as file:
        file.write(info + "\n")
    if wantSentry:
        sentry_sdk.init('https://b747c8225f394bafbdf9f830caaa293a@o1128902.ingest.sentry.io/6172162')
        from os.path import expanduser
        sentry_sdk.set_tag('district_name', os.getenv('DISTRICT_NAME', "NULL"))
        sentry_sdk.set_tag('SENDER_AVID', simbase.air.getAvatarIdFromSender())
        sentry_sdk.set_tag('SENDER_ACCOUNT_ID',simbase.air.getAccountIdFromSender())
        sentry_sdk.set_tag('homedir', expanduser('~'))
        sentry_sdk.set_tag('CRITICAL', 'True')
        sentry_sdk.capture_exception(e)
    raise
