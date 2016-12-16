

for i  in range(100,1000):
    gewei = i % 10
    shiwei = i / 10 % 10
    baiwei = i / 100

    if i == gewei **3 + shiwei **3 + baiwei **3:
        print "%d "%i,
print " "
