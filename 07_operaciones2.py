#operaciones logicas
#True (1),False (0)
#AND O &
#CONJUNCIÓN (and,&) (si tiene un falso es falso)
#number = int(input("digite un número: "))
'''
print(True and True) # =true
print(True and False) # =false
print(False and False) #false
print (number >= 3 and False and True)
print(False and False and True)
print(True & True)
'''

#DISYUNCIÓN (or,|) si tiene un true es true
'''
print(False or False) # falso
print(False or True) #verdadero
print(True or True) #verdadero
print(True or False) #verdadero
print(False or True or False)

print(number > 3 and number < 10)
print(number > 3 or True)
print(number <= 3 | number >= 10)

print(not(number <= 3 or number >= 10))
'''
#NEGACIÓN (not)
#print(not(True))

#Or EXCLUSIVA (^) es falso si hay dos valores iguales
"""
print(True ^ True)  # = False
print(False ^ False)  # = False
print(False ^ True) # = true
print(True ^ False) # = true
"""

#OPERACIONES DE RELACION O COMPARACIÓN
#number = int(input("digite un número: "))
'''
number > 3
print(number > 3)
print(number >= 3)
print(number < 3)
print(number <= 3)
print(number == 3)
print(number != 3)
'''
# OPERACIONES DE PERTENENCIA (in)
nombre = 'Juana Vera'
print('V' in nombre)
print('q' in nombre)
