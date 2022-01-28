"""EditorGlobals module: contains global editor data"""

from direct.showbase.PythonUtil import uniqueElements

# levels should put themselves into the bboard under this posting
# to assert themselves as the level to be edited by ~edit
EditTargetPostName = 'inGameEditTarget'

EntIdRange = 10000
# Once a range has been assigned to a user, please don't change it.
username2entIdBase = {
    'darren': 1 * EntIdRange,
    'samir': 2 * EntIdRange,
    'skyler': 3 * EntIdRange,
    'joe': 4 * EntIdRange,
    'DrEvil': 5 * EntIdRange,
    'asad': 6 * EntIdRange,
    'drose': 7 * EntIdRange,
    'pappy': 8 * EntIdRange,
    'patricia': 9 * EntIdRange,
    'jloehrle': 10 * EntIdRange,
    'rurbino': 11 * EntIdRange,
}
assert uniqueElements(list(username2entIdBase.values()))

usernameConfigVar = 'level-edit-username'
undefinedUsername = 'UNDEFINED_USERNAME'
editUsername = config.GetString(usernameConfigVar, undefinedUsername)

# call this to make sure things have been set up correctly


def checkNotReadyToEdit():
    # returns error string if not ready, None if ready
    if editUsername == undefinedUsername:
        return f"you must config '{usernameConfigVar}'; see {__name__}.py"
    # Feel free to add your name to the table if it's not in there
    if editUsername not in username2entIdBase:
        return f"unknown editor username '{editUsername}'; see {__name__}.py"
    return None


def assertReadyToEdit():
    msg = checkNotReadyToEdit()
    if msg is not None:
        assert False, msg


def getEditUsername():
    return editUsername


def getEntIdAllocRange():
    """range of valid entId values for this user.
    returns [min, max+1] (values taken by range() and xrange())"""
    baseId = username2entIdBase[editUsername]
    return [baseId, baseId + EntIdRange]
