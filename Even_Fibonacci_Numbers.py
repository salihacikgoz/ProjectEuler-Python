sayi1 = 0
sayi2 = 1
ciftToplam = 0

while True:
    sayi3 = sayi1 + sayi2
    if (sayi3 < 4000000):
        if (sayi3 % 2 == 0):
            ciftToplam = ciftToplam + sayi3
        sayi1 = sayi2
        sayi2 = sayi3
    else:
        break
print("Çift Toplam Sayısı: ",ciftToplam)
