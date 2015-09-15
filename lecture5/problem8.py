def isIn(char, aStr):
    if len(aStr) == 1:
        return char == aStr
    elif len(aStr) > 1:
        middle = int(len(aStr)/2)
        if aStr[middle] == char:
            return True
        elif aStr[middle] > char:
            return isIn(char, aStr[0:middle])
        else:
            return isIn(char, aStr[middle:])
    else:
        return False
