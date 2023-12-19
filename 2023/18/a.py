for q2 in [0,1]:
    tot = x = y = 0
    for D, L, H in [l.split(' ') for l in open('test.txt').readlines()]:
        x1, y1, D, L = x, y, int(H[7]) if q2 else 'RDLU'.index(D), int("0x" + H[2:7], 0) if q2 else int(L)
        x, y = [[x,y][i] + (L * -1 * (D-(i+1)) if D % 2 == i else 0) for i in range(2)]
        tot += (x1 * y - x * y1) / 2 + L / 2
    print(int(tot + 1))