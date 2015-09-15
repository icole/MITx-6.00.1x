def semordnilap(str1, str2):
    if len(str1) != len(str2):
        return False
    elif str1 == "" and str2 == "":
        return True
    else:
        if str1[0] == str2[-1]:
            return semordnilap(str1[1:], str2[0:-1])
        else:
            return False

if semordnilap("bar", "rab"):
    print "SUCCESS!"
else:
    print "NOPE!"

