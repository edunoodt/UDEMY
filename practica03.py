phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}

print (phone_numbers.keys())
print (phone_numbers.values())
print (phone_numbers.items())

for i in phone_numbers:
    print(f'{i} telefono es {phone_numbers[i]}')
 
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")
