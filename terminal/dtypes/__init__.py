def checkstring(argState: list, pos: int):
    return str(argState[pos])


def checknumber(argState: list, pos: int):
    return int(argState[pos])


def checkClass(argState: list, pos: int, classf):
    return classf(argState[pos])


# checks an argument and potentially stores it into an array parsing it using [].
def checkarray(argState: list, IsNearestInstance: bool, pos: int = 0):
    if IsNearestInstance:
        s = ' '.join(argState)
        array_cn = s[s.find("[") + 1:s.rfind("]")]
        narr = []
        for i in array_cn.split(","):
            narr.append(i)
        return narr
