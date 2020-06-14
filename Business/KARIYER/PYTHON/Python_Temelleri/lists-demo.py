# 1  - "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

arabalar = ['BMW', 'Mercedes', 'Opel', 'Mazda']
# print(arabalar)

# 2  - Liste kaç elemanlıdır?
# print(len(arabalar))

result =len(arabalar)

# 3  - Listenin ilk ve son elemanı nedir?

result = arabalar[0]  # Baştan itibaren ilk eleman.
result = arabalar[3]  # Baştan itibaren son eleman.
result = arabalar[-1] # Sondan itibaren ilk eleman (baştan sonuncu).


# 4  - Mazda değerini Totota değeri ile değiştiriniz.

arabalar[-1] = 'Toyota'
# result(arabalar)

# 5  - Mercedes listenin bir elemanı mıdır?

result = 'Mercedes' in arabalar

# 6  - Listenin -2 indexindeki değer nedir?

# result = arabalar[-2]

# 7  - Listenin ilk 3 elemanını alın.

result = arabalar[0:3]
result = arabalar[:3]
result = arabalar[-2:]

# 8  - Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.

arabalar[-2:] = ['Toyota', 'Renault']
result = arabalar

# 9  - Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

result = arabalar + ['Audi', 'Nissan']

# 10 - Listenin son elemanını silin.

del arabalar[-1]
result = arabalar

# 11 - Liste elemanlarını tersten yazdırınız.

result = arabalar[::-1]

# 12 - Aşağıdaki verileri bir liste içinde saklayınız.

     # studentA = Yiğit Bilgi 2010, (70,60,70)
     # studentB = Sena Turan 1999, (80,80,70)
     # studentC = Ahmet Turan 1998 (80,70,90)

studentA = ['Yiğit', 'Bilgi', 2010, [70,60,70]]
studentB = ['Sena', 'Turan', 1999, [80,80,70]]
studentC = ['Ahmet', 'Turan', 1998, [80,70,90]]

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result =  f"Yiğit Bilgi 10 yaşında ve not ortalaması 66"

result = f"{studentA[0]} {studentA[1]} {2020 - studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])//3}"

# 13 - Liste elemanlarını ekrana yazdırınız.    

print(result)
