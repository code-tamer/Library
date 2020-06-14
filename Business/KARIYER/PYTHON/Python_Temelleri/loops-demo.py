'''
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
    ** "random modülü" için "python random" şeklinde arama yapın. (hak = 5)
    ** 100 üzerinden puanlama yapın, her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''

# NOT-1 

# import random

# sayi = random.randint(1,100)
# hak = 5

# while hak > 0:
#     hak -= 1
#     tahmin = int(input('Tahmin: '))

#     if sayi == tahmin:
#         print('Tebrikler bildiniz.')
#         break
#     elif sayi > tahmin:
#         print('yukarı')
#     else:
#         print('aşağı')
    
#     if hak == 0:
#         print(f'hakkınız bitti, tutulan sayı {sayi}')


# NOT 2

# import random

# sayi = random.randint(1,10)
# hak = 5
# sayac = 0

# while hak > 0:
#     hak -= 1
#     sayac += 1
#     tahmin = int(input('Tahmin: '))

#     if sayi == tahmin:
#         print(f'Tebrikler, {sayac}. hakknızda bildiniz.')
#         break
#     elif sayi > tahmin:
#         print('yukarı')
#     else:
#         print('aşağı')
    
#     if hak == 0:
#         print(f'hakkınız bitti, tutulan sayı {sayi}')

# NOT 3

# import random

# sayi = random.randint(1,10)
# hak = 5
# sayac = 0

# while hak > 0:
#     hak -= 1
#     sayac += 1
#     tahmin = int(input('Tahmin: '))

#     if sayi == tahmin:
#         print(f'Tebrikler, {sayac}. hakknızda bildiniz. Toplam puanınız {100 - (20) * (sayac-1)}')
#         break
#     elif sayi > tahmin:
#         print('yukarı')
#     else:
#         print('aşağı')
    
#     if hak == 0:
#         print(f'hakkınız bitti, tutulan sayı {sayi}')


# NOT 4

import random

sayi = random.randint(1,10)
can = int(input('kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler, {sayac}. hakknızda bildiniz. Toplam puanınız {100 - (100//can) * (sayac-1)}')
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')
    
    if hak == 0:
        print(f'hakkınız bitti, tutulan sayı {sayi}')