# I thought the question was what is the longest time you could spend in the train in a day...
# Ugh...
# Have to redo it...
# Ugh...


input = [[848422, 917816], [1340021, 1637788], [2289832, 2300391], [3019734, 3061673], [3297784, 3724342], [4133812, 4379173], [5003571, 5445113], [5649842, 5650334], [5928562, 6282997], [6144832, 6633605], [6221210, 6606582], [6726587, 6803605], [7129526, 7418692], [7411908, 7518646], [7876841, 8184092], [8047427, 8176266], [8311725, 8784149], [8795408, 8930814], [9302294, 9481294], [9792964, 10193562], [10518510, 10795484], [11249830, 11674518], [12232929, 12493194], [13046739, 13280986], [13182155, 13293010], [13669421, 14095228], [14362259, 14850159], [15149525, 15382431], [15930908, 15984016], [16207950, 16267038], [16962219, 17345608], [17389321, 17727417], [17613915, 17979458], [18087911, 18337878], [18578613, 18790186], [19007968, 19280830], [19199826, 19518608], [20121415, 20254986], [20167563, 20658711], [21080568, 21364069], [21227429, 21546221], [21262617, 21401469], [22192298, 22520587], [22986728, 23456701], [23643892, 23804522], [24577392, 24907398], [25403954, 25611353], [26094059, 26385660], [26667133, 26948054], [27657783, 27973926], [27949997, 27982022], [28936682, 29265047], [29590365, 29654108], [30471058, 30708643], [30815896, 31152121], [31800017, 31960201], [32792939, 33123505], [33438334, 33906787], [34108308, 34221551], [35035443, 35529787], [35564680, 35996747], [35963458, 36392959], [36039134, 36072994], [36665928, 37020586], [37234399, 37289376], [37588433, 37814102], [38425992, 38467330], [38822354, 38996871], [39731508, 39878613], [40475374, 40864984], [41200251, 41484088], [41310130, 41999838], [42343341, 42463055], [42858894, 43269947], [43574218, 43750656], [44182412, 44561967], [44686511, 45154488], [45406308, 45591490], [45721223, 45862978], [46451934, 46949342], [47443100, 47538755], [48184557, 48498564], [49092049, 49141719], [49637439, 49812621], [50530909, 50579006], [51117366, 51350323], [51256476, 51742503], [52096066, 52445262], [52553685, 52889989], [52840345, 53193977], [53274516, 53313735], [54072684, 54338191], [54784697, 54885175], [55062923, 55471889], [55421784, 55519773], [56340867, 56377273], [56631697, 56994718], [56791595, 57087695], [57134070, 57172077], [57209345, 57212767]]
# input = [[1,2],[2,9],[9,25],[15,22]]

def find_longest_in_a_row():
    tot = []
    for i in range(len(input)):
        curr = input[i]
        tot.append(curr[1] - curr[0])

        for next in input[i+1:]:
            if next[0] >= curr[1]:
                tot[-1] += next[1] - next[0]
                curr = next
            else:
                break
        print(f'Starting at {i} ({input[i][0]}): total {tot[-1]}')
    tot.sort()
    print(f'Final: {tot[-1]}')

def find_longest_in_a_day():
    start = input[0][0]
    possible = [[start, input, 0, []]] #List of [curr_time, possible_routes, total_time, curr_route]

    best_route = []
    max_time = 0
    while len(possible) > 0:
        curr_time, pos_r, total_time, curr_route = possible[0]

        #Pop the left one, recording it if a new best route is found
        if possible[0][2] > max_time:
            max_time = possible[0][2]
            best_route = possible[0][3]
        possible = possible[1:]

        #Only keep train routes that are still possible
        pos_r = list(filter(lambda x: x[0] >= curr_time, pos_r))

        #Take first one
        if len(pos_r) > 0:
            possible.append([pos_r[0][1], pos_r[1:], total_time + pos_r[0][1] - pos_r[0][0], curr_route + [pos_r[0]]])

        #Wait until second
        if len(pos_r) > 1:
            possible.append([pos_r[1][0], pos_r[1:], total_time, curr_route])

        #Sort by start time
        possible.sort(key=lambda x: (x[0], -1*x[2]))

        #Filter out all the routes that are impossible to get the best result
        curr_max = 0
        filtered = []
        for pos in possible:
            if pos[2] > curr_max:
                curr_max = pos[2]
                filtered.append(pos)
        possible = filtered

    print(max_time)

    score = 0
    for train in input:
        start, end = train

        if train in best_route:
            score += end - start
            print(f'TAKE {start}-{end} | score -> {score}')
        else:
            print(f'SKIP {start}-{end}')


find_longest_in_a_row()
find_longest_in_a_day()