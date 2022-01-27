sayi = 0
while True:
    sayac = 0
    sayi = sayi + 1
    for i in range(1,20):
        if(sayi % i == 0):
            sayac = sayac + 1
    if(sayac == 19):
        break
print(sayi)
