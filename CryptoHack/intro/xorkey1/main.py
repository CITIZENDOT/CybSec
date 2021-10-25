from Crypto.Util.number import long_to_bytes
from itertools import permutations


def main():
    """
    FLAG starts with 'crypto{'
    data ^ key = encrypted
    So, data ^ encrypted = key
    xorring with 'crypto{' may give part of the key
    """
    s = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    s_bytes = bytes.fromhex(s)
    s_bytes_len = len(s_bytes)

    key = "myXORkey"
    key_len = len(key)
    key = ((s_bytes_len // key_len) * key) + key[: (s_bytes_len % key_len)]

    print(bytes(i ^ ord(j) for (i, j) in zip(s_bytes, key)).decode("utf-8"))


if __name__ == "__main__":
    main()
