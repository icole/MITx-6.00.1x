def uniqueValues(aDict):
    resultDict = dict(aDict)
    for key in aDict:
        if key in resultDict:
            restDict = dict(aDict)
            del restDict[key]
            for k, v in restDict.iteritems():
                if aDict[key] == v:
                    if key in resultDict:
                        del resultDict[key]
                    del resultDict[k]
    return sorted(resultDict.keys())

print uniqueValues({"a": 1, "b": 1, "d": 2, "c": 5})
print uniqueValues({1: 1, 2: 1, 3: 1})
