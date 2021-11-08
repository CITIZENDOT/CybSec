import requests

session = requests.Session()
BLOCK_SIZE = 16  # bytes


def xor_bytes(s1, s2):
    return bytes(i ^ j for (i, j) in zip(s1, s2))


def decrypt(ciphertext):
    response = session.get(
        f"http://aes.cryptohack.org/ecbcbcwtf/decrypt/{ciphertext.hex()}"
    )
    response = response.json()
    plaintext = bytes.fromhex(response["plaintext"])
    return plaintext


def main():
    response = session.get("http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag")
    response = response.json()
    ciphertext = bytes.fromhex(response["ciphertext"])
    num_blocks = len(ciphertext) // BLOCK_SIZE
    blocks = [
        ciphertext[i * BLOCK_SIZE : (i + 1) * BLOCK_SIZE] for i in range(num_blocks)
    ]

    decrypted_blocks = [decrypt(block) for block in blocks]
    for i in range(1, num_blocks):
        plaintext = xor_bytes(decrypted_blocks[i], blocks[i - 1])
        print(plaintext.decode("utf-8"), end="")
    print()


if __name__ == "__main__":
    main()
