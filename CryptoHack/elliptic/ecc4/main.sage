from sage.all import *

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1] :]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode("ascii"))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode("ascii")
    else:
        return plaintext.decode("ascii")


def main():
    E = EllipticCurve(GF(9739), [497, 1768])
    P = E.lift_x(4726)
    n_B = 6534
    shared_point = n_B * P
    x, y = shared_point.xy()
    iv = "cd9da9f1c60925922377ea952afc212c"
    ciphertext = "febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"
    print(decrypt_flag(x, iv, ciphertext))


if __name__ == "__main__":
    main()
