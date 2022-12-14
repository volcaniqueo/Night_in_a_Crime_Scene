hand = open('crime_scene.TXT')
w_dict = dict()
t_dict = dict()
val_dict = dict()
vlist = list()
ccount = 0
for line in hand:
    a = line.split()
    if ccount == 0:
        weight_limit = int(a[0])
        time_limit = int(a[1])
        ccount += 1
        continue
    if ccount == 1:
        ccount += 1
        continue
    w_dict[a[0]] = int(a[1])
    t_dict[a[0]] = int(a[2])
    val_dict[a[0]] = int(a[3])
    vlist.append(a[0])
hand.close()
count1 = len(vlist)


def val_function(templist, n=0):
    global val_dict
    if n == len(templist):
        return 0
    return val_dict[templist[n]] + val_function(templist, n + 1)


def combination_function(t_dict, vlist, w_dict, w_limit, t_limit, ver, tempw=0, tempt=0, templist=list(), call=0):
    global count1
    global comblist
    global max_val
    if count1 == call:
        if val_function(templist) > max_val:
            max_val = val_function(templist)
            comblist = list(tuple(templist))
        return
    if 2 < 5:
        if tempw + w_dict[vlist[0]] <= w_limit or ver == 't':
            if tempt + t_dict[vlist[0]] <= t_limit or ver == 'w':
                a = vlist.pop(0)
                templist.append(a)
                tempw += w_dict[a]
                tempt += t_dict[a]
                call += 1
                combination_function(t_dict, vlist, w_dict, w_limit, t_limit, ver, tempw, tempt, templist, call)
                call -= 1
                templist.pop()
                vlist.insert(0, a)
                tempw -= w_dict[a]
                tempt -= t_dict[a]
    if 5 < 8:
        a = vlist.pop(0)
        call += 1
        combination_function(t_dict, vlist, w_dict, w_limit, t_limit, ver, tempw, tempt, templist, call)
        vlist.insert(0, a)
        call -= 1


def my_sort_func(lst, n=0):
    global newlist
    if n == len(lst):
        return
    smallcount = 0
    val1 = lst.pop(n)
    for i in lst:
        if int(val1) <= int(i):
            smallcount += 1
    lst.insert(n, val1)
    newlist[len(lst) - 1 - smallcount] = val1
    my_sort_func(lst, n + 1)


comblist = []  # Part-1
max_val = 0
combination_function(t_dict, vlist, w_dict, weight_limit, time_limit, 'w')
hand1 = open('solution_part1.txt', 'w')
hand1.write(str(val_function(comblist)))
hand1.write('\n')
newlist = comblist.copy()
my_sort_func(comblist)
for abc in newlist:
    hand1.write(str(abc))
    hand1.write(' ')
hand1.close()


comblist = []  # Part-2
max_val = 0
combination_function(t_dict, vlist, w_dict, weight_limit, time_limit, 't')
hand2 = open('solution_part2.txt', 'w')
hand2.write(str(val_function(comblist)))
hand2.write('\n')
newlist = comblist.copy()
my_sort_func(comblist)
for abc in newlist:
    hand2.write(str(abc))
    hand2.write(' ')
hand2.close()


comblist = []  # Part-3
max_val = 0
combination_function(t_dict, vlist, w_dict, weight_limit, time_limit, 'wt')
hand3 = open('solution_part3.txt', 'w')
hand3.write(str(val_function(comblist)))
hand3.write('\n')
newlist = comblist.copy()
my_sort_func(comblist)
for abc in newlist:
    hand3.write(str(abc))
    hand3.write(' ')
hand3.close()






