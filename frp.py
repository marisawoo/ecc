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

def findInverse(b, prime):
    for i in range(prime):
        if (b*i)%p == 1:
            return i
    print("Did not find inverse")
    
