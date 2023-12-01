elves = [0]

for line in open('input.txt', 'r').readlines():
    if line == '\n':
        elves.append(0)
    else:
        elves[-1] += int(line)

print(sum(sorted(elves)[-3:]))
print(sum(elves.sort()[:3]))