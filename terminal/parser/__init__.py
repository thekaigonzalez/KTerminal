from typing import List


def checkquotedstring(pos, array: List[str]):
    strs = array.pop(pos)
    strst = ""
    if strs.startswith("\""):
        for i in array:
            if not i.endswith("\""):
                strst += i + " "
            elif i.endswith("\""):
                strst += i[0:len(i)-1] + " "
    return strs[1:len(strs)] + " " + strst