def oddTuples(aTup):
    newTuple = ()
    for index in range(len(aTup)):
        if index % 2 == 0:
            newTuple += (aTup[index],)
    return newTuple

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))