def main():
    x = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(x)
    a = input().upper()
    b = input().upper()
    result = ''
    i = 0
    print(b.capitalize())
    b = ''.join(b.split(' '))
    if len(a) > len(b):
        z = len(a) - len(b)
        while i < z:
            b = b + b[i]
            i += 1
    i = 0

    while i < len(''.join((a).split(' '))):
        a1 = x.index((''.join((a).split(' ')))[i])
        b1 = x.index(b[i])
        k = a1 + b1
        if k > len(x) - 1:
            k = k - len(x)
        result = result + x[k]
        i += 1
    print(result)

if __name__ == main():
    main()

### output = 'O'