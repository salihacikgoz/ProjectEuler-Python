sayac = 0

for i in range(1,600851475143):
    if(13195 % i == 0):
            for j in range(1,i + 1):
                if(i % j == 0):
                    sayac = sayac + 1
            if(sayac == 2):
                max = i
            sayac = 0
print(max)