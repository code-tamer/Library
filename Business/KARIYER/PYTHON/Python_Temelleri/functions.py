# def sayHello():
#     print('Hello')

# sayHello()

# def sayHello(name):
#     print('Hello ' + name)

# sayHello('İlker Batu')

# def sayHello(name = 'user'):
#     print('Hello ' + name)

# sayHello()

# def sayHello(name = 'user'):
#     return 'Hello ' + name
    
# msg = sayHello('İlker Batu')
# print(msg)

# def total(num1, num2):
#     return num1 + num2
# result = total(10, 20)
# print(f'İşlemin sonucu: {result}')

# def yasHesapla(dogumYili):
#     return 2020 - dogumYili

# def emekliligeKacYilKaldi(dogumYili, isim):
#     yas = yasHesapla(dogumYili)
#     emeklilik = 65 - yas
#     if emeklilik > 0:
#         print(f'Sayın {isim}, emekliliğinize {emeklilik} yıl kaldı.')
#     else:
#         print(f'Sayın {isim}, zaten emeklisiniz')
    
# emekliligeKacYilKaldi(1977, 'Tamer')

# def emekliligeKacYilKaldi(dogumYili, isim):
    # '''
    # DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldı.
    # INPUT: Dogum yili
    # OUTPUT: Hesaplanan yil bilgisi
    # '''
#     yas = yasHesapla(dogumYili)
#     emeklilik = 65 - yas
#     if emeklilik > 0:
#         print(f'Sayın {isim}, emekliliğinize {emeklilik} yıl kaldi.')
#     else:
#         print(f'Sayın {isim}, zaten emeklisiniz')
    
# emekliligeKacYilKaldi(1977, 'Tamer')

# print(help(emekliligeKacYilKaldi))

list = [1,2,3]

print(help(list.append))


