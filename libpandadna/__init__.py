import sys
if sys.platform == "darwin":
        # Create folder in /Library/Developer/Panda3D and call it pandaMac and drop libpandadna.so in there
    from pandaMac.libpandadna import *
else:
    from .libpandadna import *