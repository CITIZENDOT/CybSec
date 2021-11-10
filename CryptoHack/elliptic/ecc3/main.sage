from sage.all import *
import hashlib


def main():
    E = EllipticCurve(GF(9739), [497, 1768])
    Q_A = E(815, 3190)
    n_B = 1829
    shared_secret = str((Q_A * n_B).xy()[0])
    print(hashlib.sha1(shared_secret.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
