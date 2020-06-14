'''
    Girilen bir sayının asl sayı olup olmadığını kontrol ediniz.
    * Asal sayı sadece kendisine ve 1'e tam bölünen sayılardır.
'''

sayi = int(input('Bir Sayı Giriniz: '))
asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2, sayi):
    if (sayi %2 == 0):
        asalmi = False
        break
if asalmi:
    print('sayı asaldır')
else:
    print('sayı asal değildir')
