def fruta(**kwargs):
    print(kwargs)
    for arg in kwargs:
        print(f"\nkey: {arg}, value: {kwargs[arg]}")

fruta(fruit='Apple', coulor='Blue', sky='bird', details='Ecommerce')

abc = {
    'one': 'A',
    'two': 'B',
    'three': 'C',
}

abc_2 = {
    'air': 'plane',
    'coulor': 'red',
    'date': '2080'
}

letter = {**abc, **abc_2}

print('\n', letter, '\n')


def customer(name, lastname, email, age):
    print(f"Nombre: {name}")
    print(f"Apellido: {lastname}")
    print(f"Email: {email}")
    print(F"Edad: {age}\n")

friend = {
    'name': 'Felipe',
    'lastname': 'Diaz',
    'email': 'felipe@diaz.io',
    'age': 90
}

customer(**friend)


def my_list(fruit, number, message):
    print(f"Fruta: {fruit}")
    print(f"Numero : {number}")
    print(F"Mensaje: {message}\n")

fruta = 'Manzana'
lista = [
    44,
    'Que tal el dia'
]

my_list(fruta, *lista)

# val = ['a', 'b', 'c']

# if not 'a' in val:
#     print('Esta disponible.')
# else:
#     print('Esta en uso')
def usuarios():

    i = 0
    users = []
    user_dc = {}

    while i < 1:

        user = input('Your username: @')
        user = '@' + user.strip()
        name = input('Your name: ')
        lastname = input('Your lastname:')

        print('\n')

        user_dc[user.lower()] = {'name': name.strip(), 'lastname': lastname.strip()}

        i += 1

    return user_dc

# my_users = usuarios()
my_users = {
    '@felipe': {
        'name': 'Felipe',
        'lastname': 'Cuchipe'
    },
    '@freddy': {
        'name': 'Freddy',
        'lastname': 'Diaz'
    }
}

for username, user_info in my_users.items():
    print(f"users = (\n\t'{username}': (\n\t\t'name': '{user_info['name']}',\n\t\t'lastname': '{user_info['lastname']}'\n\t)\n)")

# users[i].append(name)
# users[i].append(lastname)
# print(users)

# users_default = []

# for user in users:
#     users_default.append(tuple(user))

# print(users_default)
