from cryptography.fernet import Fernet
import json

print("[1] - Encrypt")
print("[2] - Decrypt")
print("[3] - Make a new key")

valinta = str(input("emppu.cc @> "))

with open('config.json') as f:
    config = json.load(f)

key = config.get('key')

if valinta == "1":
    tiedosto = str(input("File: "))
    f = Fernet(key)

    with open(tiedosto, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    tiedosto2 = str('enc_')+str(tiedosto)
    with open(tiedosto2,'wb') as encrypted_file:
        encrypted_file.write(encrypted)

elif valinta == "2":
    tiedosto = str(input("File: "))
    f = Fernet(key)

    with open(tiedosto, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    try:
        decrypted = f.decrypt(encrypted)

        if tiedosto[:4] == "enc_":
            tiedosto = tiedosto[4:]
        
        tiedosto2 = str('dec_')+str(tiedosto)
        with open(tiedosto2, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

    except:
        print("[-] Wrong key")

elif valinta == "3":
    key = Fernet.generate_key()
    key = str(key,'utf-8')
    
    config["key"] = f"{key}"

    with open('config.json', 'w') as f:
        json.dump(config, f)
    
    print("[+] Key succesfully generated")

print("[+] Done")
