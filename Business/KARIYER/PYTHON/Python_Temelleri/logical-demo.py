# 1- Girilen bir sayının 0 ile 100 arasında olup olmadığını kontrol ediniz.

# x = float(input('Bir Sayı Giriniz: '))

# result = (x > 0) and (x <= 100)

# print(f'Girilen sayı sıfır ile yüz arasındadır: {result}')



# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# y = int(input('Bir Sayı Giriniz: '))

# result = (y > 0) and (y %2 == 0)

# print(f'Girdiğiniz sayı pozitif ve çift bir sayıdır: {result}')



# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'tamer.sahin@galatasaray.net'
# password = 'abc123'

# girilenEmail = input('email: ')
# girilenPassword = input('password: ')

# result = (email == girilenEmail) and (password == girilenPassword)

# print(f'Girilen email adresi ve parola doğrudur: {result}')



# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input('a:' ))
# b = int(input('b:' ))
# c = int(input('c:' ))

# result = (a > b) and (a > c)
# print(f'a en büyük sayıdır: {result}')

# result = (b > a) and  (b > c)
# print(f'b en büyük sayıdır: {result}')

# result = (c > a) and (c > b)
# print(f'c en büyük sayıdır: {result}')



# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamasını hesaplayınız;
#    Eğer ortalama 50 ve üstünde ise geçti, değilse kaldı yazdırınız.
#    a-) Ortalama 50 olsa bile final notu 50 olmalıdır.
#    b-) Final 70 olduğunda ortalamanın önemi olmasın.

# vize1 = float(input('vize 1:' ))
# vize2 = float(input('vize 2:' ))
# final = float(input('final:' ))

# ortalama = ((vize1 + vize2) /2) * 0.60 + (final) * 0.40

# # result = (ortalama >= 50) and (final >= 50) (sorunun a seçeneğindeki koşul)

# result = (ortalama >= 50) or (final >= 70) (sorunun b seçeneğindeki koşul)

# print(f'öğrencinin not ortalaması: {ortalama} ve geçme durumu: {result}')



# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir;
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

# name = input('Adınız: ')
# weight = float(input('Kilonuz: '))
# height = float(input('Boyunuz: '))  # (Kiloyu girerken örn 1.80 diye girmek lazım ondalıklı olarak)

# index = (weight) / (height ** 2) 

# zayif = (0 < index) and (index <= 18.4)
# normal = (18.5 < index) and (index <= 24.9)
# kilolu = (25.0 < index) and (index <=29.9)
# obez = (30.0 < index) and (index <= 34.0)

# print(f'{name} indexiniz: {index} ve değerlendirmeniz zayıf: {zayif} ')
# print(f'{name} indexiniz: {index} ve değerlendirmeniz normal: {normal} ')
# print(f'{name} indexiniz: {index} ve değerlendirmeniz kilolu: {kilolu} ')
# print(f'{name} indexiniz: {index} ve değerlendirmeniz obez: {obez} ')



