def xor_bytes(a: bytes, b: bytes):
    return bytes(i ^ j for i, j in zip(a, b))


def main():
    s = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    s_bytes = bytes.fromhex(s)
    for i in range(0, 256):
        data = bytes(byte ^ i for byte in s_bytes)
        try:
            possible_flag = data.decode("utf-8")
            if possible_flag.startswith("crypto{"):
                print(possible_flag)
                break
        except:
            pass


if __name__ == "__main__":
    main()
