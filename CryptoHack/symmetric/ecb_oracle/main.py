from string import ascii_lowercase, digits, punctuation
import requests


def encrypt(session, plaintext):
    if session is None:
        session = requests
    plaintext = plaintext.encode("utf-8")
    response = session.get(
        f"http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext.hex()}"
    )
    return bytes.fromhex(response.json()["ciphertext"])


def main():
    session = requests.Session()
    BLOCK_SIZE = 16
    PLAINTEXT_LENGTH = 31
    printable = ascii_lowercase + digits + punctuation

    curr = ""
    while True:
        len_curr = len(curr)
        block_index = ((len_curr) // 16) + 1
        plaintext = "1" * (PLAINTEXT_LENGTH - (len_curr % 16))
        start_point = block_index * BLOCK_SIZE
        cipher1 = encrypt(session, plaintext)

        if len(cipher1) == (start_point + BLOCK_SIZE):
            break
        else:
            print(len(cipher1), start_point + BLOCK_SIZE)

        print(f"Current Flag = {curr} Length = {len_curr}")
        print(f"PlainText = {plaintext} Length = {len(plaintext)}")
        print(f"Block Index = {block_index}")

        for char in printable:
            print(f"\tTesting {char} ...", end=" ")
            cipher2 = encrypt(session, plaintext + curr + char)
            if (
                cipher1[start_point : start_point + BLOCK_SIZE]
                == cipher2[start_point : start_point + BLOCK_SIZE]
            ):
                print("Passed")
                curr += char
                break
            else:
                print("Failed")
        else:
            print(f"Character not found!")
            exit(-1)
    print(f"Success: {curr}")


if __name__ == "__main__":
    main()

# crypto{p3n6u1n5_h473_3cb}
