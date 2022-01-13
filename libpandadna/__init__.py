import sys

if sys.platform == "darwin":
        # Create folder in /Library/Developer/Panda3D and call it pandaMac and drop panda3d.toontown.so in there
    from pandaMac.panda3d.toontown import *
else:
    from .panda3d.toontown import *