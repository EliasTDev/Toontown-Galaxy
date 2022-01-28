# -------------------------------------------------------------------------------
# Contact: Rob Gordon
# Created: Oct 2008
#
# Purpose: This module provides mixin classes (mostly individual states) for
#          use with ActivityFSM.
# -------------------------------------------------------------------------------

"""
This module provides mixin classes (mostly individual states) for use with
ActivityFSM.  Functionality is provided in this manner to avoid massive code
duplication that would occur otherwise.
"""

# parties imports
from .BaseActivityFSM import BaseActivityFSM

# --------------------------------------------------------------------------
# Idle State
# --------------------------------------------------------------------------


class IdleMixin:
    def enterIdle(self, *args):
        BaseActivityFSM.notify.info(
            f"enterIdle: '{self.oldState}' -> '{self.newState}'")
        if len(args) > 0:
            self.activity.startIdle(*args)
        else:
            self.activity.startIdle()

    def filterIdle(self, request, args):
        BaseActivityFSM.notify.debug(
            f"filterIdle( '{request}', '{args}' )")
        if request == "Idle":
            return None
        else:
            return self.defaultFilter(request, args)

    def exitIdle(self):
        BaseActivityFSM.notify.debug(
            f"exitIdle: '{self.oldState}' -> '{self.newState}'")
        self.activity.finishIdle()

# --------------------------------------------------------------------------
# Active State
# --------------------------------------------------------------------------


class ActiveMixin:
    def enterActive(self, *args):
        BaseActivityFSM.notify.info(
            f"enterActive: '{self.oldState}' -> '{self.newState}'")
        if len(args) > 0:
            self.activity.startActive(*args)
        else:
            self.activity.startActive()

    def filterActive(self, request, args):
        BaseActivityFSM.notify.debug(
            f"filterActive( '{request}', '{args}' )")
        if request == "Active":
            return None
        else:
            return self.defaultFilter(request, args)

    def exitActive(self):
        BaseActivityFSM.notify.debug(
            f"exitActive: '{self.oldState}' -> '{self.newState}'")
        self.activity.finishActive()

# --------------------------------------------------------------------------
# Disabled State
# --------------------------------------------------------------------------


class DisabledMixin:
    def enterDisabled(self, *args):
        BaseActivityFSM.notify.info(
            f"enterDisabled: '{self.oldState}' -> '{self.newState}'")
        if len(args) > 0:
            self.activity.startDisabled(*args)
        else:
            self.activity.startDisabled()

    def filterDisabled(self, request, args):
        BaseActivityFSM.notify.debug(
            f"filterDisabled( '{request}', '{args}' )")
        if request == "Disabled":
            return None
        else:
            return self.defaultFilter(request, args)

    def exitDisabled(self):
        BaseActivityFSM.notify.debug(
            f"exitDisabled: '{self.oldState}' -> '{self.newState}'")
        self.activity.finishDisabled()


# --------------------------------------------------------------------------
# Rules State
# --------------------------------------------------------------------------
class RulesMixin:
    def enterRules(self, *args):
        BaseActivityFSM.notify.info(
            f"enterRules: '{self.oldState}' -> '{self.newState}'")
        if len(args) > 0:
            self.activity.startRules(*args)
        else:
            self.activity.startRules()

    def filterRules(self, request, args):
        BaseActivityFSM.notify.debug(
            f"filterRules( '{request}', '{args}' )")
        if request == "Rules":
            return None
        else:
            return self.defaultFilter(request, args)

    def exitRules(self):
        BaseActivityFSM.notify.debug(
            f"exitRules: '{self.oldState}' -> '{self.newState}'")
        self.activity.finishRules()


# --------------------------------------------------------------------------
# WaitForEnough State
# --------------------------------------------------------------------------
class WaitForEnoughMixin:
    def enterWaitForEnough(self, *args):
        BaseActivityFSM.notify.info(
            f"enterWaitForEnough: '{self.oldState}' -> '{self.newState}'")
        if len(args) > 0:
            self.activity.startWaitForEnough(*args)
        else:
            self.activity.startWaitForEnough()

    def filterWaitForEnough(self, request, args):
        BaseActivityFSM.notify.debug(
            f"filterWaitForEnough( '{request}', '{args}' )")
        if request == "WaitForEnough":
            return None
        else:
            return self.defaultFilter(request, args)

    def exitWaitForEnough(self):
        BaseActivityFSM.notify.debug(
            f"exitWaitForEnough: '{self.oldState}' -> '{self.newState}'")
        self.activity.finishWaitForEnough()


# --------------------------------------------------------------------------
# WaitToStart State
# --------------------------------------------------------------------------
class WaitToStartMixin:
    def enterWaitToStart(self, *args):
        BaseActivityFSM.notify.info(
            f"enterWaitToStart: '{self.oldState}' -> '{self.newState}'")
        if len(args) > 0:
            self.activity.startWaitToStart(*args)
        else:
            self.activity.startWaitToStart()

    def filterWaitToStart(self, request, args):
        BaseActivityFSM.notify.debug(
            f"filterWaitToStart( '{request}', '{args}' )")
        if request == "WaitToStart":
            return None
        else:
            return self.defaultFilter(request, args)

    def exitWaitToStart(self):
        BaseActivityFSM.notify.debug(
            f"exitWaitToStart: '{self.oldState}' -> '{self.newState}'")
        self.activity.finishWaitToStart()


# --------------------------------------------------------------------------
# WaitClientsReady State
# --------------------------------------------------------------------------
class WaitClientsReadyMixin:
    def enterWaitClientsReady(self, *args):
        BaseActivityFSM.notify.info(
            f"enterWaitClientsReady: '{self.oldState}' -> '{self.newState}'")
        if len(args) > 0:
            self.activity.startWaitClientsReady(*args)
        else:
            self.activity.startWaitClientsReady()

    def filterWaitClientsReady(self, request, args):
        BaseActivityFSM.notify.debug(
            f"filterWaitClientsReady( '{request}', '{args}' )")
        if request == "WaitClientsReady":
            return None
        else:
            return self.defaultFilter(request, args)

    def exitWaitClientsReady(self):
        BaseActivityFSM.notify.debug(
            f"exitWaitClientsReady: '{self.oldState}' -> '{self.newState}'")
        self.activity.finishWaitClientsReady()

# --------------------------------------------------------------------------
# WaitForServer State
# --------------------------------------------------------------------------


class WaitForServerMixin:
    def enterWaitForServer(self, *args):
        BaseActivityFSM.notify.info(
            f"enterWaitForServer: '{self.oldState}' -> '{self.newState}'")
        if len(args) > 0:
            self.activity.startWaitForServer(*args)
        else:
            self.activity.startWaitForServer()

    def filterWaitForServer(self, request, args):
        BaseActivityFSM.notify.debug(
            f"filterWaitForServer( '{request}', '{args}' )")
        if request == "WaitForServer":
            return None
        else:
            return self.defaultFilter(request, args)

    def exitWaitForServer(self):
        BaseActivityFSM.notify.debug(
            f"exitWaitForServer: '{self.oldState}' -> '{self.newState}'")
        self.activity.finishWaitForServer()


# --------------------------------------------------------------------------
# Conclusion State
# --------------------------------------------------------------------------
class ConclusionMixin:
    def enterConclusion(self, *args):
        BaseActivityFSM.notify.info(
            f"enterConclusion: '{self.oldState}' -> '{self.newState}'")
        if len(args) > 0:
            self.activity.startConclusion(*args)
        else:
            self.activity.startConclusion()

    def filterConclusion(self, request, args):
        BaseActivityFSM.notify.debug(
            f"filterConclusion( '{request}', '{args}' )")
        if request == "Conclusion":
            return None
        else:
            return self.defaultFilter(request, args)

    def exitConclusion(self):
        BaseActivityFSM.notify.debug(
            f"exitConclusion: '{self.oldState}' -> '{self.newState}'")
        self.activity.finishConclusion()
