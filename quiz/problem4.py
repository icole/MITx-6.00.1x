def evalQuadratic(a, b, c, x):
    return a * (x * x) + b * x + c

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    return evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)

a1 = -9.3
b1 = -6.72
c1 = -3.1
x1 = 9.03
a2 = -7.29
b2 = 8.67
c2 = -4.27
x2 = -3.58

print twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2)