# sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayılar listesini while ile ekrana yazdırınız.
# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp bu aralıktaki
#    tüm tek sayıları ekrana yazdırınız.

# baslangic = int(input('başlangıç: '))
# bitis = int(input('bitiş: '))

# i = baslangic

# while i < bitis:
#     i += 1
#     if (i % 2 == 1):
#         print(i)


# 3- 1 ile 100 arasındaki sayıları azalan şekilde ekrana yazdırınız.

# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekran sıralı bir şekilde yazdırınız.

# numbers = []
# i = 0
# while i<5:
#     sayi = int(input('sayı: '))
#     numbers.append(sayi)
#     i+=1
# numbers.sort()
# print(numbers)


# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    * Ürün sayısını kullanıcıya sorunuz.
#    ** Dictionary listesi yapısı (name, price) şeklind olsun.
#    *** Ürün eklem işlemi bittiğinde ürünleri ekrana while ile listeleyin.

# urunler = []

# adet = int(input('kaç ürün eklemek istiyorsunuz: '))

# i = 0

# while(i<adet):
#     name = input('ürün ismi: ')
#     price = input('ürün fiyatı: ')
#     urunler.append({
#         'name': name,
#         'price': price
#     })
#     i += 1

# for urun in urunler:
#     print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')
