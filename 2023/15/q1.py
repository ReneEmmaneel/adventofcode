print(sum([(ord(x)*17)%256 for x in open('input.txt', 'r').read().split(',')]))