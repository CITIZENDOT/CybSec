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
    """
    we need to find x such that, (a * x) === 1 mod n ---> eq(1)
    we know, (a * x) + (b * y) = gcd(a, b)           ---> eq(2)
    coefs for eq(2) exists only if gcd(a, n) = 1 (from eq(1))
    from eq(1), (a * x) + (b * n) = 1                ---> eq(3)
    we need to find x from eq(3) (we can find x and b by extended_gcd)
    """
    a = 3
    b = 13
    u, v, g = extended_gcd(a, b)
    print(u)


if __name__ == "__main__":
    main()
