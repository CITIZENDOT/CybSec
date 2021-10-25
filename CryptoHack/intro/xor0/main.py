def main():
    s = "label"
    n = 13
    xorred = "".join([chr(ord(i) ^ n) for i in s])
    print(xorred)


if __name__ == "__main__":
    main()
