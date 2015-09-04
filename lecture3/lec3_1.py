num = 0
while num <= 5:
    print num
    num += 1

print "Outside of loop"
print num


num = 10
while True:
    if num < 7:
        print 'Breaking out of loop'
        break
    print num
    num -= 1
print 'Outside of loop'
