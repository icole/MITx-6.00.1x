balance = 4773
annualInterestRate = 0.2

monthlyPayment = 10
startingBalance = balance
while True:
    for i in range(1, 13):
        remainingBalance = balance - monthlyPayment
        remainingBalance += (remainingBalance * annualInterestRate)/12
        balance = remainingBalance
    if balance > 0:
        balance = startingBalance
        monthlyPayment += 10
    else:
        break

print "Lowest Payment: " + str(monthlyPayment)
