from pwn import *
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1] :]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode("ascii"))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode("ascii")
    else:
        return plaintext.decode("ascii")


def main():
    io = remote("socket.cryptohack.org", 13371)

    e = 3  # MITM exponent

    alice_data = io.recvlineS(keepends=False)
    alice_data = json.loads(alice_data[24:])
    p, g, A = map(lambda x: int(alice_data[x], 16), ["p", "g", "A"])

    # Sendind to bob
    io.clean()
    alice_data["A"] = hex(pow(g, e, p))
    io.send_raw(json.dumps(alice_data).encode("utf-8"))

    bob_data = io.recvlineS(keepends=False)
    bob_data = json.loads(bob_data[22:])
    B = int(bob_data["B"], 16)
    bob_shared_secret = pow(B, e, p)

    # Sending to alice
    io.clean()
    bob_data["B"] = hex(pow(g, e, p))
    alice_shared_secret = pow(A, e, p)
    io.send_raw(json.dumps(bob_data).encode("utf-8"))

    flag_details = io.recvlineS(keepends=False)
    flag_details = json.loads(flag_details[24:])
    io.close()
    print(
        decrypt_flag(
            alice_shared_secret, flag_details["iv"], flag_details["encrypted_flag"]
        )
    )


if __name__ == "__main__":
    main()
