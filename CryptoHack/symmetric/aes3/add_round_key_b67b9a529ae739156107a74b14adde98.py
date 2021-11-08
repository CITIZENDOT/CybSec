import numpy as np

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def matrix2bytes(matrix):
    """Converts a 4x4 matrix into a 16-byte array."""
    matrix = np.array(matrix)
    plaintext_bytes = matrix.flatten()
    return "".join([chr(i) for i in plaintext_bytes])


def add_round_key(s, k):
    s = np.array(s)
    k = np.array(k)
    return matrix2bytes(s ^ k)


print(add_round_key(state, round_key))
