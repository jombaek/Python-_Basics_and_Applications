from simplecrypt import decrypt, DecryptionException

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

passwords = []

with open("passwords.txt", "r") as txt:
    for line in txt:
        passwords.append(line.strip())

for pwd in passwords:
    try:
        print(pwd)
        print(decrypt(pwd, encrypted).decode('utf8'))
    except DecryptionException:
        pass