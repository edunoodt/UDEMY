phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}

print (phone_numbers.keys())
print (phone_numbers.values())
print (phone_numbers.items())

for i in phone_numbers:
    print(f'{i} telefono es {phone_numbers[i]}')
 
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")

phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")

phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for valor in phone_numbers.values():
    print(valor.replace('+','00'))





















































