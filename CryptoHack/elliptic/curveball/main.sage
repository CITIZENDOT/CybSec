from sage.all import *
from fastecdsa.point import Point
import json


def main():
    # Source: https://kel.bz/post/sage-p256/
    # Finite field prime
    p256 = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF

    # Curve parameters for the curve equation: y^2 = x^3 + a256*x +b256
    a256 = p256 - 3
    b256 = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B

    # Base point (x, y)
    gx = 0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296
    gy = 0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5

    # Curve order
    qq = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
    # Create a finite field of order p256
    FF = GF(p256)

    # Define a curve over that field with specified Weierstrass a and b parameters
    EC = EllipticCurve([FF(a256), FF(b256)])

    # Since we know P-256's order we can skip computing it and set it explicitly
    EC.set_order(qq)

    # Create a variable for the base point
    G = EC(FF(gx), FF(gy))

    # Bing's public key
    public_key = EC(
        0x3B827FF5E8EA151E6E51F8D0ABF08D90F571914A595891F9998A5BD49DFA3531,
        0xAB61705C502CA0F7AA127DEC096B2BBDC9BD3B4281808B3740C320810888592A,
    )
    private_key = int(3)
    new_G = list(public_key.division_points(private_key)[0].xy())
    new_G = [int(new_G[0]), int(new_G[1])]
    packet = {
        "private_key": private_key,
        "host": "www.bing.com",
        "public_key": [
            int(
                "0x3B827FF5E8EA151E6E51F8D0ABF08D90F571914A595891F9998A5BD49DFA3531", 16
            ),
            int(
                "0xAB61705C502CA0F7AA127DEC096B2BBDC9BD3B4281808B3740C320810888592A", 16
            ),
        ],
        "generator": new_G,
        "curve": "secp256r1",
    }
    print(json.dumps(packet))


if __name__ == "__main__":
    main()
