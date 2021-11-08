import requests

session = requests.Session()


def check_admin(cookie, iv):
    response = session.get(
        f"http://aes.cryptohack.org/flipping_cookie/check_admin/{cookie.hex()}/{iv.hex()}"
    )
    return response.json()


def get_cookie():
    response = session.get("http://aes.cryptohack.org/flipping_cookie/get_cookie")
    response = response.json()
    ciphertext = bytes.fromhex(response["cookie"])
    cookie, iv = ciphertext[16:], ciphertext[:16]
    return cookie, iv


def xor_bytes(s1, s2, s3):
    return bytes(i ^ j ^ k for (i, j, k) in zip(s1, s2, s3))


def main():
    cookie, iv1 = get_cookie()
    iv2 = xor_bytes(b"admin=False;expi", iv1, b"admin=True;expii")
    response = check_admin(cookie, iv2)
    print(response)


if __name__ == "__main__":
    main()
