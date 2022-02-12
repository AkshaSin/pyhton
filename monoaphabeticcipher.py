import string
plaintext = "i love india"
key= "foxabcdeghijklmnpqrstuvwyz"
cipher=""

for c in plaintext:
    if c in string.ascii_lowercase:
        index= ord(c) - ord('a')
        cipher= cipher + key[index]
    else:
        cipher = cipher +c
print("plaintext : " + plaintext)
print("cypher : " + cipher)