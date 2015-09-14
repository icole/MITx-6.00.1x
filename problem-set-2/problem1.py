balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalPayment = 0
for i in range(1, 13):
    print "Month: " + str(i)
    minimumPayment = balance * monthlyPaymentRate
    totalPayment += minimumPayment
    print "Minimum monthly payment: %.2f" % minimumPayment
    remainingBalance = balance - minimumPayment
    remainingBalance += (remainingBalance * annualInterestRate)/12
    print "Remaining balance: %.2f" % remainingBalance
    balance = remainingBalance
print "Total paid: %.2f" % totalPayment
print "Remaining balance: %.2f" % balance
