def aptab(inp, table):
    """
 >>> apply_table("0123456789", list(range(10)))
 '9012345678'
 >>> apply_table("0123456789", list(range(9, -1, -1)))
 '8765432109'
 """
    res = ""
    for i in table:
        res += inp[i - 1]
    return res

def left_shift(d):
    """
 >>> left_shift("0123456789")
 '1234567890'
 """
    return d[1:] + d[0]

def XOR(x, y):
    """
 >>> XOR("01010101", "00001111")
 '01011010'
 """
    result = ""
    for i in range(len(x)):
        if x[i] == y[i]:
            result += "0"
        else:
            result += "1"
    return result

def apply_sbox(s, d):
    col = int("0b" + d[1:3], 2)
    row = int("0b" + d[0] + d[-1], 2)
    return bin(s[row][col])[2:]

def function(expansion, s0, s1, key, message):
    left = message[:4]
    right = message[4:]
    temp = aptab(right, expansion)
    temp = XOR(temp, key)

    l = apply_sbox(s0, temp[:4])  # noqa: E741
    r = apply_sbox(s1, temp[4:])
    l = "0" * (2 - len(l)) + l  # noqa: E741
    r = "0" * (2 - len(r)) + r
    temp = aptab(l + r, p4_table)
    temp = XOR(left, temp)
    return temp + right

if __name__ == '__main__':
    key = input("Enter the 10 bit key: ")
    message = input("Enter the 8 bit message: ")
    p8_table = [6, 3, 7, 4, 8, 5, 10, 9]
    p10_table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p4_table = [2, 4, 3, 1]
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    exp = [4, 1, 2, 3, 2, 3, 4, 1]
    s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
    # key generation
    temp = aptab(key, p10_table)
    left = temp[:5]
    right = temp[5:]
    left = left_shift(left)
    right = left_shift(right)
    key1 = aptab(left + right, p8_table)
    left = left_shift(left)
    right = left_shift(right)
    left = left_shift(left)
    right = left_shift(right)
    key2 = aptab(left + right, p8_table)
    # encryption
    temp = aptab(message, IP)
    temp = function(exp, s0, s1, key1, temp)
    temp = temp[4:] + temp[:4]
    temp = function(exp, s0, s1, key2, temp)
    CT = aptab(temp, IP_inv)
    print("Cipher text is:", CT)
    # decryption
    temp = aptab(CT, IP)
    temp = function(exp, s0, s1, key2, temp)
    temp = temp[4:] + temp[:4]
    temp = function(exp, s0, s1, key1, temp)
    PT = aptab(temp, IP_inv)
    print("Plain text after decrypting is:", PT)