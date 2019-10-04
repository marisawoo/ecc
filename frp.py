# find E(F), where F is a field, more specifically F = Z_p, p prime
# E(F) : set of F-rational points on elliptic curve E
# E : Y^2 = X^3 + AX + B

def findSet(prime, a, b):
    frp = [0]
    for y in range(prime):
        for x in range(prime):
            lhs = (y**2)%prime
            rhs = (x**3 + a*x + b)%prime
            if (lhs == rhs):
                frp.append((x, y))
    print("cardinality: {0}".format(len(frp)))
    return frp

def findFRPSize(prime, a, b):
    frp = findSet(prime, a, b)
    length = len(frp)
    return length

# if lambda = a/b, then lambda = a*b^-1 mod p where b^-1 = x s.t. bx is congruent to 1 mod p
def findInverse(b, prime):
    for i in range(prime):
        if (b*i)%prime == 1:
            return i
    print("Did not find inverse")

def getLambda(x1, y1, x2, y2, a, prime):
    if (x1 == x2) and (y1 == y2):
        numerator = 3*(x1**2) + a
        denominator = 2*y1
    else: # point P does not equal point Q
        numerator = y2 - y1
        denominator = x2 - x1
    if numerator%denominator != 0:
        lam = numerator * findInverse(denominator, prime)
    else: # lambda is an integer
        lam = numerator/denominator
    return lam

def pointAdd(x1, y1, x2, y2, a, prime):
    if (x1 == x2) and ((y1+y2)%prime == 0):
        return 0
    else:
        lam = getLambda(x1, y1, x2, y2, a, prime)
        x = lam**2 - x1 - x2
        y = lam*(x1-x) - y1
        return [x%prime, y%prime]

# assumes k >= 0, k integer
def pointMult(x1, y1, a, b, prime, k):
    frpSize = findFRPSize(prime, a, b)
    scalar = k%frpSize
    point = [0, 0]
    if scalar == 0:
        return [0, 0]
    elif scalar == 1:
        return [x1, y1]
    for i in range(scalar):
        if i == 1:
            point = pointAdd(x1, y1, x1, y1, a, prime)
        else:
            point = pointAdd(point[0], point[1], x1, y1, a, prime)
    return point

def checkPrime(p):
    divisor = p//2
    while p >= 1:
        if p%divisor == 0:
            return False
        else:
            divisor -= 1
    return True
