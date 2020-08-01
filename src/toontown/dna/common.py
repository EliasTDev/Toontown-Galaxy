# Embedded file name: libpandadna\common.py

#Can't Believe You Didn't Make This A .Py Orginally.

from panda3d.core import *

def dgi_extract_string8(dgi):
    return dgi.extractBytes(dgi.getUint8())


def dgi_extract_color(dgi):
    return tuple((dgi.getUint8() / 255.0 for _ in range(4)))