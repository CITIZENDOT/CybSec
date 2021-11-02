def extended_gcd(a: int, b: int):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        qoutient = old_r // r
        old_r, r = r, old_r - (qoutient * r)
        old_s, s = s, old_s - (qoutient * s)
        old_t, t = t, old_t - (qoutient * t)
    return (old_s, old_t, old_r)


def main():
    p = 26513
    q = 32321
    u, v, _ = extended_gcd(p, q)
    print(min(u, v))


if __name__ == "__main__":
    main()
