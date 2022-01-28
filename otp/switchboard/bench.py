import sys
import os
import time


import Pyro.util
import Pyro.core
import Pyro.naming

Pyro.core.initClient()

ns = Pyro.naming.NameServerLocator().getNS()

wedge1 = Pyro.core.getProxyForURI("PYRONAME://:sb.wedge.bench")
wedge2 = Pyro.core.getProxyForURI("PYRONAME://:sb.wedge.tt")

iters = 5000

players = []

wedge2.enterPlayer(1, 0)
# for i in range(iters):
#    wedge2.enterPlayer(i,0)
#    #time.sleep(0.025)

time.sleep(5)

print('-------- BENCHMARK REMOTE OBJECT ---------')
begin = time.time()
# for f in funcs:
voor = time.time()
# wedge1._setOneway(["sendWhisper"])
for i in range(iters):
    # wedge._setOneway("sendWhisper")
    wedge1.sendWhisper(1, 1, "test")
    # players.append(Pyro.core.getProxyForURI("PYRONAME://:sb.player.%d"%i))
    # print i
    # sys.stdout.flush()
    ##testP = Pyro.core.getProxyForURI("PYRONAME://:sb.player.%d"%i)
    # players[i]._setOneway("recvWhisper")
    ##players[i].recvWhisper(5678,"Hey it's me")

try:
    duration = time.time() - begin
    print(f'total time {duration:.4f} seconds')
    print('total method calls', iters)
    avg_pyro_msec = 1000.0 * duration / (iters)
    print(f'avg. time per method call: {avg_pyro_msec:.4f}', "msec")
    print(f'msg/sec: {iters / duration:.4f}')
except BaseException:
    pass
sys.stdout.flush()
time.sleep(5)
wedge2.exitPlayer(1)
# for i in range(iters):
#    wedge2.exitPlayer(i)
