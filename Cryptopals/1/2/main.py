def xor_bytes(s1, s2):
    return bytes(i ^ j for (i, j) in zip(s1, s2))


def main():
    s1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    s2 = bytes.fromhex("686974207468652062756c6c277320657965")
    print(xor_bytes(s1, s2).hex())


if __name__ == "__main__":
    main()
