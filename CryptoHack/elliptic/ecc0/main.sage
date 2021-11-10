from sage.all import *


def main():
    # E: Y2 = X3 + 497 X + 1768, p: 9739
    E = EllipticCurve(GF(9739), [497, 1768])
    P = E(8045, 6936)
    Q = -P
    print(Q)


if __name__ == "__main__":
    main()
