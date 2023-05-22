from os import system
system('cls')

names = ["john smith", "jay santi", "eva kuki"]

new_names = [name.title() for name in names]

print (new_names)

usernames = ["john 1990", "alberta1970", "magnola2000"]

print([len(name) for name in usernames])

user_entries = ['10', '19.1', '20']

print( [float(entry) for entry in user_entries])

nueva_flot = [float(entry) for entry in user_entries]

print (sum(nueva_flot))

temperatures = [10, 12, 14]

temperatures = [str(i) + '\n' for i in temperatures]

file = open(r"Datos\file.txt", 'w')
file.writelines(temperatures)

numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)

for index, numero in enumerate(numbers):
    print (index ,' - ',numero)

