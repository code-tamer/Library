x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x, y, z toplamının farkı nedir?

# a = int(input('1. sayı: '))
# b = int(input('2. sayı: '))

# result = (a*b) - (x+y+z)


# 2- y'nin x'e kalansız bölümünü hesaplayınız.

# result = y // x

# 3- (x, y, z) toplamının mod3'ü nedir?

# result = (x+y+z) %3 => ben böyle yaptım

# toplam = (x+y+z)
# result = toplam %3    =>   bunu da anlatan yaptı

# 4- y'nin x. kuvvetini hesaplayınız.

# result = y **x

# 5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır?

x, *y, z = numbers
# print(x, y, z)
# result = z **3

# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?

result = y[0] + y[1] + y[2]

print(result)
