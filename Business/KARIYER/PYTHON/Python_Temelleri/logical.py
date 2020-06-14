# x = 5
# result = 5 <= x < 10


x = 6

result = 5 < x < 10

hak = 5
devam = 'e'

# print(result)

# and

# True, True => True
# True, False => False

result = (x > 5) and (x < 10)  

result = (hak > 0) and (devam == 'e')


# or

# True, True => True
# True, False => True
# False, False => False

result = (x > 5) or (x %2 == 0)

# not
result = not(x > 0)

# result = ((x >0) and (x<10) and (x %2 == 0))
# result = ((x >0) or (x<10) and (x %2 == 0))


print(result)