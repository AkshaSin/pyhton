
if __name__ == '__main__':
    P = 23
    G = 5
    a = 4
    b = 3
    x = int(pow(G, a, P))
    y = int(pow(G, b, P))
    ka = int(pow(y, a, P))
    kb = int(pow(x, b, P))
    print('The Value of P is :%d' % (P))
    print('The Value of G is :%d' % (G))
    print('The Private Key a for Alice is :%d' % (a))
    print('The Private Key b for Bob is :%d' % (b))
    print('Secret key for the Alice is : %d' % (ka))
    print('Secret Key for the Bob is : %d' % (kb))