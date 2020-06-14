# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma durumu en az 18 veğitim durumu
#    lise ya da üniversite olmalıdır.

# name =input('Ad: ')
# age = int(input('Yaş: '))
# edu = input('Eğitim Durumu: ')

# if (age > 18):
#     if (edu == 'lise') or (edu == 'üniversite'):
#         print(f'Sayın {name} ehliyet almaya uygundur.')
#     else:
#         print(f'Sayın {name} eğitim durumunuz ehliyet almaya uygun değildir')
# else:
#     print(f'Sayın {name} yaşınız ehliyet almaya uygun değildir.')    


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0-24   =>  0
#    25-44  =>  1 
#    45-54  =>  2
#    55-69  =>  3
#    70-84  =>  4
#    85-100 =>  5

# name = input('İsminiz: ')
# yazili1 = float(input('1. Yazılı: '))
# yazili2 = float(input('2. Yazılı: '))
# sozlu = float(input('Sözlü: '))
# ortalama = float((yazili1) + (yazili2) + (sozlu)) // 3

# if (ortalama >= 0) and (ortalama <= 24):
#     print(f'Notunuz: 0 ve Ortalamanız: {ortalama}')

# elif (ortalama >= 25) and (ortalama <= 44):
#     print(f'Notunuz: 1 ve Ortalamanız: {ortalama}')

# elif (ortalama >= 45) and (ortalama <= 54):
#     print(f'Notunuz: 2 ve Ortalamanız: {ortalama}')

# elif (ortalama >= 55) and (ortalama <= 69):
#     print(f'Notunuz: 3 ve Ortalamanız: {ortalama}')

# elif (ortalama >= 70) and (ortalama <= 84):
#     print(f'Notunuz: 4 ve Ortalamanız: {ortalama}')

# elif (ortalama >= 85) and (ortalama <= 100):
#     print(f'Notunuz: 5 ve Ortalamanız: {ortalama}')
# else:
#     print('Yanlış bir değer girdiniz')


# 3- Trafiğe çıkış tarihi alınan aracın servis zamanını aşağıdaki bilgilere 
#    göre hesaplayınız.
#    1. Bakım => 1. yıl 
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#    *** datetime modülünü kullanmamız gerekiyor.
#    (simdi) - (2018/8/1)

# days = int(input('Aracınız Kaç Gündür Trafikte: '))

# if (days <= 365):
#     print('Aracınızın 1. Bakım zamanı gelmiştir.')
# elif (days > 365 ) and (days < 365*2):
#     print('Aracınızın 2. Bakım zamanı gelmiştir.')
# elif (days > 365*2 ) and (days < 365*3):
#     print('Aracınızın 3. Bakım zamanı gelmiştir.')
# else:
#     print('Yanlış Bilgi Girdiniz')

import datetime

tarih = input('Aracınız Hangi Tarihte Trafiğe Çıktı (2019/11/4: ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if (days <= 365):
    print('Aracınızın 1. Bakım zamanı gelmiştir.')
elif (days > 365 ) and (days < 365*2):
    print('Aracınızın 2. Bakım zamanı gelmiştir.')
elif (days > 365*2 ) and (days < 365*3):
    print('Aracınızın 3. Bakım zamanı gelmiştir.')
else:
    print('Yanlış Bilgi Girdiniz')







