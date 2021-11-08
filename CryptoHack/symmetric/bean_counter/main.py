import requests

session = requests.Session()
BLOCK_SIZE = 16


def xor_bytes(s1, s2):
    return bytes(i ^ j for (i, j) in zip(s1, s2))


def main():
    response = session.get("http://aes.cryptohack.org/bean_counter/encrypt")
    response = response.json()
    encrypted = bytes.fromhex(response["encrypted"])

    num_blocks = len(encrypted) // BLOCK_SIZE
    blocks = [
        encrypted[i * BLOCK_SIZE : (i + 1) * BLOCK_SIZE] for i in range(num_blocks)
    ]

    # First 16 bytes are same for every PNG file.
    png_header = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"
    value = xor_bytes(blocks[0], png_header)

    decrypted = []
    for block in blocks:
        decrypted.append(xor_bytes(block, value))
    decrypted = b"".join(decrypted)

    with open("bean_flag.png", "wb") as f:
        f.write(decrypted)


if __name__ == "__main__":
    main()
