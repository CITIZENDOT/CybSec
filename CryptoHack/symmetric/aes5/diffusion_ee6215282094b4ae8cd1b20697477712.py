import numpy as np


def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


def inv_shift_rows(s):
    # Works for any square matrix, not just 4x4
    s = np.array(s)
    _, num_cols = s.shape
    for i in range(num_cols):
        s[:, i] = np.concatenate((s[-i:, i], s[:-i, i]), axis=0)
    return s


# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(matrix_col):
    # see Sec 4.1.2 in The Design of Rijndael
    t = matrix_col[0] ^ matrix_col[1] ^ matrix_col[2] ^ matrix_col[3]
    u = matrix_col[0]
    matrix_col[0] ^= t ^ xtime(matrix_col[0] ^ matrix_col[1])
    matrix_col[1] ^= t ^ xtime(matrix_col[1] ^ matrix_col[2])
    matrix_col[2] ^= t ^ xtime(matrix_col[2] ^ matrix_col[3])
    matrix_col[3] ^= t ^ xtime(matrix_col[3] ^ u)
    return matrix_col


def mix_columns(matrix):
    for i in range(4):
        matrix[i] = mix_single_column(matrix[i])
    return matrix


def inv_mix_columns(matrix):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(matrix[i][0] ^ matrix[i][2]))
        v = xtime(xtime(matrix[i][1] ^ matrix[i][3]))
        matrix[i][0] ^= u
        matrix[i][1] ^= v
        matrix[i][2] ^= u
        matrix[i][3] ^= v

    matrix = mix_columns(matrix)
    return matrix


def matrix2bytes(matrix):
    """Converts a 4x4 matrix into a 16-byte array."""
    if type(matrix) == list:
        matrix = np.array(matrix)
    plaintext_bytes = matrix.flatten()
    return "".join([chr(i) for i in plaintext_bytes])


state = [
    [108, 106, 71, 86],
    [96, 62, 38, 72],
    [42, 184, 92, 209],
    [94, 79, 8, 54],
]

state = inv_mix_columns(state)
state = inv_shift_rows(state)
print(matrix2bytes(state))
