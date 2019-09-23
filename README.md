# Elliptic-Curve-Calculator
Elliptic curve: E(Fp): Y^2 =X^3+AX+B \
More specifically F = Z_p, p prime
Note: It is not checked if p is a prime, please enter a number that is prime.

```findSet(prime, a, b)``` returns the set of F-rational points on E and prints the cardinality of the set. 

```findFRPSize(prime, a, b)``` returns the cardinality of F-rational points on E.

```pointAdd(x1, y1, x2, y2, a, prime)``` returns the result of point addition P + Q for 2 valid points on E, P=(x1, y1), Q=(x2, y2).

```pointMult(x1, y1, a, b, prime, k)``` returns the result of point multiplication kP for a valid point P on E, P=(x1, y1).

Run with Python console.
