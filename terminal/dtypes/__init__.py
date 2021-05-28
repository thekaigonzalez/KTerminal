def checkstring(argState: list, pos: int):
    return str(argState[pos])


def checknumber(argState: list, pos: int):
    return int(argState[pos])


def checkClass(argState: list, pos: int, classf):
    return classf(argState[pos])
