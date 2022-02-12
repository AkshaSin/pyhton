import random
def check_prime(a):
    if a == 2:
        return True
    elif a < 2 or a % 2 == 0:
        return False
    elif a > 2:
        for i in range(2, a):
            if a % i == 0:
                return False
    return True
def gcd(e, r):
    while r != 0: e, r = r, e % r
    return e
def coprime(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False
def calc_private_key(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1
def manual_input():
    global p, q
p = int(input("Enter 1st prime number : "))
q = int(input("Enter 2nd prime number : "))
while coprime(p, q) is False: manual_input()
manual_input()
print(f"\nThe value of p : {p}\nThe value of q : {q}")
n = p * q
z = (p - 1) * (q - 1)
e = 0
i = random.randrange(2, z)
while not check_prime(i):
    i = random.randrange(2, z)
else:
    e = i
print("The value of e is:", e)
private_key = calc_private_key(e, z)
