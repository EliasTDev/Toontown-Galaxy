
# The AI side
import os
import TestClientRepository
from . import DistributedTestAI
from .AIStart import *
start()
dt = DistributedTestAI.DistributedTestAI(simbase.air)
dt.setA(5)
dt.setB("hello")
dt.generateWithRequired(101)

# The Client side
# Create a test repository
basePath = os.path.expandvars('$TOONTOWN') or './toontown'
cr = TestClientRepository.TestClientRepository(
    basePath + "/src/configfiles/toon.dc")
# Connect the test repository
cr.connect("localhost", 6667)
# Set the Shard
cr.sendSetShardMsg(2000000)
# Switch to zone 101
cr.sendSetZoneMsg(101)
