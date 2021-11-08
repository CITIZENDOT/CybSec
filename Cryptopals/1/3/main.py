from string import printable


def xor_one_byte(s, ch):
    return bytes(i ^ ord(ch) for i in s)


def main():
    s = bytes.fromhex(
        "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    )
    for char in printable:
        print(xor_one_byte(s, char))


if __name__ == "__main__":
    main()
