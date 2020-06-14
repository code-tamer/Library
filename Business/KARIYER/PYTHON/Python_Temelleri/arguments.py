# def changeName(n):
#     n = 'Batu'
# name = 'Tülay'
# print(name)

# def changeName(n):
#     n = 'Batu'
#     print(n)
# name = 'Tülay'
# changeName(name)

# def change(n):
#     n[0] = 'İstanbul'
# sehirler = ['Sivas', 'Batman']
# change(sehirler)
# print(sehirler)

# sehirler = ['Sivas', 'Batman']
# n = sehirler
# n[0] = 'İstanbul'
# print(sehirler)

# sehirler = ['Sivas', 'Batman']
# n = sehirler[:]
# n[0] = 'İstanbul'
# print(n)
# print(sehirler)

# def change(n):
#     n[0] = 'İstanbul'
# sehirler = ['Sivas', 'Batman']
# change(sehirler[:])
# print(sehirler)

# def add (a,b):
#     return sum((a,b))
# print(add(10,20))

# def add (a,b):
#     return sum((a,b))
# print(add(10,20,30))

# def add (a,b,c=0):
#     return sum((a,b))
# print(add(10,20,30))

# def add (a,b,c=0):
#     return sum((a,b,c))

# print(add(10,20,30))

# def add (*params):
#     return sum((params))
# print(add(10,20,30,50,60,10,20))

# def add (*params):
#     print(params)
#     return sum((params))
# print(add(10,20,30,50,60,10,20))

# def add (*params):
#     print(params[0])
#     print(params[2])
#     return sum((params))
# print(add(10,20,30,50,60,10,20))

# def add (*params):
#     print(type(params))
#     sum = 0
#     for n in params:
#         sum = sum + n
#     return sum
# print(add(10,20,30,50,60,10,20))

# def displayUser(**args):
#     for key, value in args.items():
#         print('{} is {}' .format (key, value))

# displayUser(name = 'İlker Batu', age = '4', city = 'İstanbul')
# displayUser(name = 'Tülay', age = '29', city = 'Batman', email = 'tulay@gmail.com')
# displayUser(name = 'Tamer', age = '43', city = 'Zara', email = 'tamer@gmail.com', phone = '555 444 3322')

def displayUser(**args):
    for key, value in args.items():
        print(type(args))
        print('{} is {}' .format (key, value))

displayUser(name = 'İlker Batu', age = '4', city = 'İstanbul')
displayUser(name = 'Tülay', age = '29', city = 'Batman', email = 'tulay@gmail.com')
displayUser(name = 'Tamer', age = '43', city = 'Zara', email = 'tamer@gmail.com', phone = '555 444 3322')



    
