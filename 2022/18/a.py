S = set([tuple([int(x) for x in l.strip().split(',')]) for l in open('input.txt').readlines()])

tot = 0
for (x,y,z) in S:
    for a,b,c in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
        tot += int(not (x+a, y+b, z+c) in S)
print(tot)

OUT = set()
IN = set()
def outside(x,y,z):
    SEEN = set()
    all = [[x,y,z]]

    while len(all) > 0:
        curr = all.pop(0)

        if tuple(curr) in OUT or min(curr) < 0 or max(curr) > 30:
            OUT.update(SEEN)
            return 1

        if tuple(curr) in IN:
            break

        if tuple(curr) in SEEN or tuple(curr) in S:
            continue

        SEEN.add(tuple(curr))

        for a,b,c in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            all.append([curr[0]+a, curr[1]+b, curr[2]+c])

    IN.update(SEEN)
    return 0

tot = 0
for (x,y,z) in S:
    for a,b,c in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
        tot += int(outside(x+a, y+b, z+c))
print(tot)