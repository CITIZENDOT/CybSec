def gcd(a: int, b: int):
    if b != 0:
        return gcd(b, a % b)
    return a


def main():
    a = 66528
    b = 52920
    print(gcd(b, a))


if __name__ == "__main__":
    main()
