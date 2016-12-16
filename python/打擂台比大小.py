
l = [[4,8,5,7],[7,8,4,7],[1,7,8,6]]

max = l[0][0]
x = y = 0
for i in range(3):
    for j in range(4):
        if l[i][j] > max:
            max = l[i][j]
            x = y
            y = j
print "l[%d][%d] = %d"%(x,y,max)
