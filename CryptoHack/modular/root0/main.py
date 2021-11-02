def main():
    p = 29
    ints = [14, 6, 11]

    for i in ints:
        is_quadratic_residue = False
        square_root = 0
        for j in range(p):
            if pow(j, 2, p) == i:
                is_quadratic_residue = True
                square_root = j
                break
        if is_quadratic_residue:
            print(i, square_root)


if __name__ == "__main__":
    main()
