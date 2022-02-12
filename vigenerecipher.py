message = 'HHWKSWXSLGNTCG'
key = 'PASCAL'
encode_test = ''
decoded = ''
for i in range(len(message)):
    def words(letter):
        return (ord(letter.upper())-64)
    key += key
    encode_test += key[i]
    decoded += chr((((words(message[i])-words(key[i])) % 26))+65)
print(message)
print(encode_test)
print(decoded)