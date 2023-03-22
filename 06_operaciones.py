#OPERACIONES ARITMATICAS
#SUMA +,RESTA -,MULTI *,div/, DIV ENTERO //
#MODULO O RESIDUO %,POTENCIACION **,
#JERARQUIA
# 1. (),2. **,3.*/,4. +-
number = int(input("digite un número: "))
print(f'la suma con 2 es:{number+2}')
print(f'la resta con 2 es:{number-2}')
print(f'la multiplicación por 2 es:{number*2}')
print(f'la división con 2 es:{number/2}')
print(f'la división ENTERA con 2 es:{number//2}')
print(f'el residuo con 2 es:{number % 2}')
print(f'la división con 2 es:{number**2}')
#OPERACIONES ASIGNACIÓN
number += 1
print(f'operador incremental += resultado es:{number}')
number -= 1
print(f'operador decremental -= resultado es:{number}')
number *= 2
print(f'al usar el operador *= el resultado es:{number}')
number /= 2
print(f'al usar el operador /= el resultado es:{number}')
number //= 2
print(f'al usar el operador //= el resultado es:{number}')
number %= 2
print(f'al usar el operador %= el resultado es:{number}')
number **= 2
print(f'al usar el operador **= el resultado es:{number}')
