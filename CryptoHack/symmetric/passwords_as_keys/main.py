import hashlib
import requests
from Crypto.Cipher import AES


def main():
    session = requests.Session()
    ciphertext = bytes.fromhex(
        "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
    )
    response = session.get(
        "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
    )
    words = response.content.splitlines()
    for word in words:
        key = hashlib.md5(word).digest()
        cipher = AES.new(key, AES.MODE_ECB)
        try:
            decrypted = cipher.decrypt(ciphertext).decode()
            if decrypted.startswith("crypto"):
                print(decrypted)
        except Exception as e:
            pass


if __name__ == "__main__":
    main()
