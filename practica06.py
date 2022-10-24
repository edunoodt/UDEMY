"""
mi_arch = open ('textos/fruits.txt')
print (mi_arch.read())
mi_arch.close()
"""

with open('textos/fruits.txt') as mi_arch:
    print(mi_arch.read())