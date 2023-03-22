# condicional if
#if('prueba lógica')
adivinar=42
numero = int(input('Sr usuario,digite un número:'))
if (numero > adivinar):
  print('bajele al volumen')
elif(numero < adivinar): 
  print('subale al volumen')
else:
  print("VERDADERO")

if(numero >= adivinar):
  if(numero > adivinar):
    print('coloque un número menor')
  else:
    print("acertado")
else:
  print("coloque un número mayor")
    
  
  
print("la instrucción termino")
 