l = [[4,8,2,7],
     [4,8,5,2],
     [7,9,4,5]]

for i in range(3):
    line_max = max(l[i])
    k = l[i].index(line_max)
    num = l[i][k]
    for j in range(3):
        if l[j][k] > num:
            num = l[j][k]
    if num == line_max:
        print "l[%d][%d] = %d"%(i,k,num)
