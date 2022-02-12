dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext = 'Hello'
plaintext = plaintext.upper()
key = 'XMCKL'
ciphertext = ''
decoded = ''
for i in range(len(plaintext)):
    if plaintext[i] in dict and key[i] in dict:
        Pi = dict.index(plaintext[i])
        Ki = dict.index(key[i])
        Ci = ((Pi + Ki) % 26)
        ciphertext += dict[Ci]
print(ciphertext)

for i in range (len(ciphertext)):
    if ciphertext[i] in dict and key[i] in dict:
        Pi = dict.index(ciphertext[i])
        Ki = dict.index(key[i])
        Di = ((Pi - Ki) % 26)
        decoded += dict[Di]
print(decoded)
