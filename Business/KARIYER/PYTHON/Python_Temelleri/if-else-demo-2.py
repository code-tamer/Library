# # 1- Girilen bir sayının 0 ile 100 arasında olup olmadığını kontrol ediniz.

# x = float(input('Bir Sayı Giriniz: '))

# if (x > 0) and (x <= 100):
#     print('Girdiğiniz Sayı 0 ile 100 Arasındadır')
# else:
#     print('Girdiğiniz Sayı 0 ile 100 Arasında Değildir')



# # 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# y = int(input('Bir Sayı Giriniz: '))

# if (y > 0):
#     if (y %2 == 0):
#         print('Girdiğiniz Sayı Pozitif Çift Sayıdır.')
#     else:
#         print('Girdiğiniz Sayı Pozitif Ancak Tek Sayıdır.')
# else:
#     print('Girdiğiniz Sayı Negatiftir.')


# # 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'tamer.sahin@galatasaray.net'
# password = 'abc123'

# girilenEmail = input('email: ')
# girilenPassword = input('password: ')

# if (girilenEmail == email):
#     if(girilenPassword == password):
#         print('Hoşgeldiniz')
#     else:
#         print('Parola Yanlış')
# else:
#     print('Email Yanlış')



# # 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input('a:' ))
# b = int(input('b:' ))
# c = int(input('c:' ))

# Benim çözümüm aşağıdaki gibi;

# if (a > b) and (a > c):
#     print('a en büyük sayıdır')
# elif (b > a) and  (b > c):
#     print('b en büyük sayıdır')
# else: 
#     print('c en büyük sayıdır')

# Anlatıcının çözümü ise;

# if (a > b) and (a > c):
#     print('a en büyük sayıdır')
# elif (b > a) and  (b > c):
#     print('b en büyük sayıdır')
# elif (c > a) and (c > b):
#     print('c en büyük sayıdır')




# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamasını hesaplayınız;
#    Eğer ortalama 50 ve üstünde ise geçti, değilse kaldı yazdırınız.
#    a-) Ortalama 50 olsa bile final notu 50 olmalıdır.
#    b-) Final 70 olduğunda ortalamanın önemi olmasın.

# vize1 = float(input('vize 1: '))
# vize2 = float(input('vize 2: '))
# final = float(input('final: '))

# ortalama = ((vize1 + vize2) /2) * 0.60 + (final) * 0.40

# # if (ortalama >= 50):   # (sorunun a seçeneğindeki koşul)
# #     if (final >= 50):
# #         print(f'öğrencinin not ortalaması: {ortalama} ve geçme durumu: Başarılı')
# #     else:
# #         print(f'öğrencinin not ortalaması: {ortalama} ve geçme durumu: Başarısız. Finalden en az 50 almanız zoruludur.')
# # else:
# #     print(f'öğrencinin not ortalaması: {ortalama} ve geçme durumu: Başarısız')

# if (ortalama >= 50):   # (sorunun b seçeneğindeki koşul)
#         print(f'öğrencinin not ortalaması: {ortalama} ve geçme durumu: Başarılı')
# else:
#     if (final >= 70):
#         print(f'öğrencinin not ortalaması: {ortalama} ve geçme durumu: Başarılı. Finalden en az 70 aldığınız için geçtiniz.')
#     else:
#         print(f'öğrencinin not ortalaması: {ortalama} ve geçme durumu: Başarısız')
        

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir;
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Kilolu
#    30.0-34.9 => Şişman (Obez)

# name = input('Adınız: ')
# weight = float(input('Kilonuz: '))
# height = float(input('Boyunuz: '))  # (Boyu girerken örn 1.80 diye girmek lazım ondalıklı olarak)

# index = (weight) / (height ** 2)

# if (index > 0) and (index <= 18.4):
#     print(f'{name} indexiniz: {index} ve değerlendirmeniz zayıf.')
# elif (index > 18.4) and (index <= 24.9):
#     print(f'{name} indexiniz: {index} ve değerlendirmeniz normal.')
# elif (index > 24.9) and (index <= 29.9):
#     print(f'{name} indexiniz: {index} ve değerlendirmeniz kilolu.')
# elif (index > 29.9) and (index <= 34.9):
#     print(f'{name} indexiniz: {index} ve değerlendirmeniz obez.')
# else:
#     print('Bilgileriniz Yanlış')




