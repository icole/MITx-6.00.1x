def lenRecur(aStr):
    length = 0
    if aStr == '':
        return length
    else:
        return 1 + lenRecur(aStr[1:])

print str(lenRecur('asdsd'))
