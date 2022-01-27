max = 0
for i in range(100,1000):
    for j in range(100,1000):
        test = i * j
        a = str(test)
        if(test == int(a[::-1])):
            if(max < test):
                max = test
print(max)

