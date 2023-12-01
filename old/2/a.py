from utils import lmap, ints, strs

f = ['A', 'B', 'C']
s = ['X', 'Y', 'Z']

def points(a,b):
    fs = f.index(a)
    sn = s.index(b)
    
    ff = (fs + sn - 1 )%3

    print(ff)
    
    return sn * 3 + ff + 1



a = 0 
for l in open('input.txt', 'r').readlines():
    #print(*strs(l))
    #print(points(*strs(l)))
    a += points(*strs(l))
print(a)