plaintext = "110011"
key = "101010"

enc = (bin(int(plaintext,2) ^ int(key,2)))[2::]
print(f'Encrypted --> {enc}')

dec = (bin(int(enc,2) ^ int(key,2)))[2::]
print(f'decryption --> {dec}')