# find E(F), where F is a field, more specifically F = Z_p, p prime
# E(F) : set of F-rational points on elliptic curve E
# E : Y^2 = X^3 + 8X + 15

def findSet(p):
    frp = [0]
    for y in range(p):
        for x in range(p):
            ok = (y**2)%p
            hello = (x**3 + 8*x + 15)%p
            if (ok == hello):
                frp.append((x, y))
    print("cardinality: {0}".format(len(frp)))
    return frp


    
