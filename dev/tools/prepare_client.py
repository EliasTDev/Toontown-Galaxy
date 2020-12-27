from pandac.PandaModules import *
import argparse
import os

os.chdir('../../')


parser = argparse.ArgumentParser()
parser.add_argument('--build-dir', default='build',
                    help='The directory in which to store the build files.')
parser.add_argument('--src-dir', default='.',
                    help='The directory of the Toontown Galaxy source code.')
parser.add_argument('modules', nargs='*', default=['otp', 'toontown'],
                    help='The Toontown Galaxy modules to be included in the build.')
args = parser.parse_args()

print('Preparing the client...')

# Create a clean build directory for us to store our build material:
if not os.path.exists(args.build_dir):
    os.mkdir(args.build_dir)
print('Build directory = {0}'.format(args.build_dir))



# Copy the provided Toontown modules:

# All client and server files are included by default.
includes = ('NonRepeatableRandomSourceUD.py', 'NonRepeatableRandomSourceAI.py')

# This is a list of explicitly excluded files.
excludes = ('ServiceStart.py', 'ToontownUberRepository.py', 'ToontownAIRepository.py')

def minify(f):
    """
    Returns the "minified" file data with removed __debug__ code blocks.
    """

    data = ''

    debugBlock = False  # Marks when we're in a __debug__ code block.
    elseBlock = False  # Marks when we're in an else code block.

    # The number of spaces in which the __debug__ condition is indented:
    indentLevel = 0

    for line in f:
        thisIndentLevel = len(line) - len(line.lstrip())
        if ('if __debug__:'.encode('latin-1') not in line) and (not debugBlock):
            data += line.decode('latin-1')
            continue
        elif 'if __debug__:'.encode('latin-1') in line:
            debugBlock = True
            indentLevel = thisIndentLevel
            continue
        if thisIndentLevel <= indentLevel:
            if 'else'.encode('latin-1') in line:
                elseBlock = True
                continue
            if 'elif'.encode('latin-1') in line:
                line = line[:thisIndentLevel] + line[thisIndentLevel+2:]
            data += line.decode('latin-1')
            debugBlock = False
            elseBlock = False
            indentLevel = 0
            continue
        if elseBlock:
            data += line[4:].decode('latin-1')

    return data

for module in args.modules:
    print('Writing module...', module)
    for root, folders, files in os.walk(os.path.join(args.src_dir, module)):
        outputDir = root.replace(args.src_dir, args.build_dir)
        if not os.path.exists(outputDir):
            os.mkdir(outputDir)
        for filename in files:
            if filename in includes:
                if not filename.endswith('.py'):
                    continue
                if not filename.endswith('UD.py'):
                    continue
                if not filename.endswith('AI.py'):
                    continue
                if not filename in excludes:
                    continue
            with open(os.path.join(root, filename), 'rb') as f:
                data = minify(f)
            with open(os.path.join(outputDir, filename), 'wb') as f:
                f.write(data.encode('latin-1'))

# Let's write _gamedata.py now. _gamedata is a compiled collection
# of data that will be used by the game at runtime. It contains
# the PRC file data and the stripped DC file for the client side.

# First, we need the PRC file data:
configFileName = 'local.prc'
configData = []
print('Using config file: {0}'.format(configFileName))

# Next, we need the (stripped) DC file:
dcFile = DCFile()
filepath = os.path.join(args.src_dir, 'etc')
for filename in os.listdir(filepath):
    if filename.endswith('.dc'):
        dcFile.read(Filename.fromOsSpecific(os.path.join(filepath, filename)))
dcStream = StringStream()
dcFile.write(dcStream, True)
dcData = dcStream.getData()

# Finally, write our data to _gamedata.py:
print('Writing _gamedata.py...')
gameData = '''\
CONFIG = %r
DC = %r'''
with open(os.path.join(args.build_dir, '_gamedata.py'), 'w') as f:
    f.write(gameData % (configData, dcData))

print('Done preparing the client.')
