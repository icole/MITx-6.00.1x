balance = 999999
annualInterestRate = 0.18

minPayment = balance / 12
maxPayment = (balance + (balance * annualInterestRate)) / 12
monthlyPayment = (minPayment + maxPayment) / 2
startingBalance = balance
while True:
    for i in range(1, 13):
        remainingBalance = balance - monthlyPayment
        remainingBalance += (remainingBalance * annualInterestRate)/12
        balance = remainingBalance
    if balance > 0.01:
        balance = startingBalance
        minPayment = monthlyPayment
        monthlyPayment = (minPayment + maxPayment) / 2
    elif balance < 0:
        balance = startingBalance
        maxPayment = monthlyPayment
        monthlyPayment = (minPayment + maxPayment) / 2
    else:
        break

print "Lowest Payment: %.2f" % monthlyPayment
