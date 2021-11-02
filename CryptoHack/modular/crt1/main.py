def main():
    """
    x ≡ 2 mod 5
    x ≡ 3 mod 11
    x ≡ 5 mod 17
    """
    congruencies = [(2, 5), (3, 11), (5, 17)]
    N = 1
    for i in congruencies:
        N *= i[1]
    x = 0
    for i in congruencies:
        Mi = N // i[1]
        x += i[0] * pow(Mi, -1, i[1]) * (Mi)
    print(x % N)


if __name__ == "__main__":
    main()
