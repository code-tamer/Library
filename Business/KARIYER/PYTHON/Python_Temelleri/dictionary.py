# # key - value
# # 41 => kocaeli, 34 => istanbul

# sehirler=['kocaeli','istanbul']
# plakalar=[41,43]

# # print(plakalar[sehirler.index('kocaeli')])

# # print(plakalar['kocaeli']) => 41
# # print(plakalar['istanbul']) => 34

# plakalar = {'kocaeli':41, 'istanbul':34}

# # print(plakalar['kocaeli'])
# # print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'
# print(plakalar)

users = {
    'sadikturan':{
        'age':36,
        'roles':['user'],
        'email':'sadik@gmail.com',
        'address':'kocaeli',
        'phone':'12345678'
    },
    'cinarturan':{
        'age':2,
        'roles': ['admin','user'],
        'email':'cinar@gmail.com',
        'address':'kocaeli',
        'phone':'12345678'
    }

}

# print(users['cinarturan']['age'])
# print(users['cinarturan']['email'])
# print(users['cinarturan']['address'])

print(users['cinarturan']['roles'][0])




