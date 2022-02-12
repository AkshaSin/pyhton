plain_text = input("Enter plain text:")
col = int(input("Enter columns:"))
key = input("Enter key:")
plain_text = plain_text.replace(" ","")
plain_text = plain_text+'xyz'

k = list(key.split(" "))
cipher_text = ''

for i in k:
    t = int(i)-1
    while t<len(plain_text):
        cipher_text += plain_text[t]
        t = t+col

print('Cipher text:', cipher_text)

decrypted='APTMTTNAAODWTSUOCOIXKNLYPETZ'
print(decrypted==cipher_text.upper())