from sage.all import *


def main():
    p = (2 ^ 255) - 19
    E = EllipticCurve(GF(p), [0, 486662, 0, 1, 0])
    P = E.lift_x(9)
    n = 0x1337C0DECAFE
    print((n * P).xy())


if __name__ == "__main__":
    main()
