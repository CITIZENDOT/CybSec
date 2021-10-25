import base64


def main():
    s = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    s_bytes = bytes.fromhex(s)
    encoded = base64.encodebytes(s_bytes)
    print(encoded)


if __name__ == "__main__":
    main()
