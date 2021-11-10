from sage.all import *


def main():
    E = EllipticCurve(GF(9739), [497, 1768])
    P = E(2339, 2213)
    print(7863 * P)


if __name__ == "__main__":
    main()
