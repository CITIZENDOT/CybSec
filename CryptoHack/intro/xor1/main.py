def xor_bytes(a: bytes, b: bytes):
    return bytes(i ^ j for i, j in zip(a, b))


def main():
    # KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
    # KEY2 ^ KEY1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
    # KEY2 ^ KEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
    # FLAG ^ KEY1 ^ KEY3 ^ KEY2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

    KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
    KEY2 = xor_bytes(
        KEY1, bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
    )
    KEY3 = xor_bytes(
        KEY2, bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
    )
    FLAG = xor_bytes(
        xor_bytes(
            xor_bytes(
                bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"),
                KEY1,
            ),
            KEY2,
        ),
        KEY3,
    )
    print(FLAG.decode("utf-8"))


if __name__ == "__main__":
    main()
