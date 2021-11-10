class EllipticCurve:
    def __init__(self, A, B, p):
        self.A = A
        self.B = B
        self.p = p
        discri = ((4 * pow(A, 3, p)) + (27 * pow(B, 2, p))) % p
        assert discri != 0, "Curve is Singular"

    def check(self, x, y):
        LHS = pow(y, 2, self.p)
        RHS = pow(x, 3, self.p) + (self.A * x) + self.B
        return (LHS % self.p) == (RHS % self.p)

    def __eq__(self, E) -> bool:
        return self.A == E.A and self.B == E.B and self.p == E.p


class EllipticPoint:
    def __init__(self, E: EllipticCurve, x, y, check=True):
        self.E = E
        self.x = x
        self.y = y
        if check and (not E.check(x, y)):
            raise Exception("Point is not the curve")

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, P):
        assert self.E == P.E, "Other point is not on same curve"
        if self.x == P.x and self.y == -P.y:
            return (0, 1)
        elif (self.x != P.x) or (self.y != P.y):
            l = (P.y - self.y) * pow(P.x - self.x, -1, self.E.p)
        else:
            l = ((3 * (self.x ** 2)) + self.E.A) * pow(2 * self.y, -1, self.E.p)
        x3 = (l ** 2) - self.x - P.x
        y3 = l * (self.x - x3) - self.y
        return EllipticPoint(self.E, x3 % self.E.p, y3 % self.E.p)


def main():
    A = 497
    B = 1768
    p = 9739
    E = EllipticCurve(A, B, p)

    P = EllipticPoint(E, 493, 5564)
    Q = EllipticPoint(E, 1539, 4742)
    R = EllipticPoint(E, 4403, 5202)

    print(P + P + Q + R)


if __name__ == "__main__":
    main()
