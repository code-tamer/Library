# name = "Tamer"
# surname = "Şahin"
# age= 43

# print("My name is " + name + " " + surname + " and I am " + str(age) + " years old. ")
# yukarıdaki kodu çalıştırdığımızda ekrenda My name is Tamer Şahin and I am 43 years old sonucunu alırız.
# and'den sonrakini kısmı bir alt satırda görmek istersen kodu aşağıdaki şekilde değiştiririz.

# print("My name is " + name + " " + surname + " and \nI am " + str(age) + " years old. ")
# bu kodu yeni bir değişken gibi tanımlayıp run edersek yine aynı sonucu alırız;

name = "Tamer"
surname = "Şahin"
age= 43

greeting = "My name is " + name + " " + surname + " and \nI am " + str(age) + " years old."
lenght = len(greeting)


# print(greeting)

print(greeting[0])
print(len(greeting))

#son karakteri yazdıralım greeting karakterinin

# print(greeting[lenght-1])
# print(greeting [-1])

# print(greeting [3:5])

# print(greeting [3: ])
# print(greeting [ :15])

print(greeting [2:40:2])






