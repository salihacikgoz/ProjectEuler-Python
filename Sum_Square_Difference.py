toplam = 0
toplamCift = 0
for i in range(1,101):
    toplam = toplam + (i ** 2)
    toplamCift = toplamCift + i
print((toplamCift ** 2) - toplam)