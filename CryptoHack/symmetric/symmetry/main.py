import requests


session = requests.Session()


def main():
    response = session.get("http://aes.cryptohack.org/symmetry/encrypt_flag")
    response = response.json()
    ciphertext = bytes.fromhex(response["ciphertext"])
    iv, encrypted = ciphertext[:16], ciphertext[16:]

    response = session.get(
        f"http://aes.cryptohack.org/symmetry/encrypt/{encrypted.hex()}/{iv.hex()}"
    )
    response = response.json()
    plaintext = bytes.fromhex(response["ciphertext"])
    print(plaintext.decode("utf-8"))


if __name__ == "__main__":
    main()
