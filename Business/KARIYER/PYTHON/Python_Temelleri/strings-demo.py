website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- "course" karakter dizisinde kaç karakter bulunmaktadır ?

result = len(course)
lenght = len(website)

# 2- "website" içinde www karakterlerini alın.

#result = website[7:10]

# 3- "website" içinde com karakterlerini alın.

result = website[lenght-3:lenght]

# 4- "course" içinden ilk 15 ve son 15 karakterlerini alın.
result = course[0:15]
result = course[-15:]


# 5- "course" ifadesindeki arakterleri tersten yazdırın.
result = course[::-1]
s = "12345"
print(s[::5])

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın;
#  "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis"
result = "Benim adım" + " " + name + " " +surname + ", Yaşım" + " " + str(age) + " ve mesleğim" + " " + job
result = "Benim adım {} {} , Yaşım {} ve mesleğim {}.".format(name,surname, age,job)
result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}."

# 7- "Hello world" ifadesindeki w yi W ile değiştirin.
s = "Hello world"

s = s[0:6] + "W" + s[-4:]
print(s)

# 8- "abc" ifadesini yanyana 3 defa yazdırın.

result = "abc" * 3


print(result)














