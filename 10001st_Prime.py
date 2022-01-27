sayac = 0
i = 0
while True:
    i = i + 1
    asalChk = 0
    for j in range(1,i):
        if(i % j == 0):
           asalChk = asalChk + 1
    if(asalChk == 1):
       sayac = sayac + 1
    if(sayac == 10001):
        print(i)
        break

