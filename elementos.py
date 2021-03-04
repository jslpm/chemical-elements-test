import random
import numpy as np

# Elementos quimicos

elementos = {1: ['H', 'HIDROGENO', 'HIDRÓGENO'],
             2: ['He', 'HELIO'],
             3: ['Li', 'LITIO'],
             4: ['Be', 'BERILIO'],
             5: ['B', 'BORO'],
             6: ['C','CARBONO'],
             7: ['N', 'NITROGENO'],
             8: ['O', 'OXIGENO'],
             9: ['F', 'FLUOR'],
            10: ['Ne', 'NEON'],
            11: ['Na', 'SODIO'],
            12: ['Mg', 'MAGNESIO'],
            13: ['Al', 'ALUMINIO'],
            14: ['Si', 'SILICIO'],
            15: ['P', 'FOSFORO']}

answer= 'start'
corrects = 0
errors = 0
values = np.arange(15)

while values.size != 0:
  randNum = random.choice(values) 
  element = elementos[randNum + 1][1]
  symbol = elementos[randNum + 1][0]
  
  print(f'¿Cuál es el símbolo del {element}?')
  print('Ingresa tu respueta (0 para salir):')
  answer = str(input())
   
  if answer == '0':
    break

  if answer == symbol:
    values = np.delete(values, np.where(values==randNum))
    #print(f'values vector: {values}')
    print('¡Muy bien!\n')
    corrects += 1
  else:
    errors += 1
    print('Incorrecto\n')

print('\n-----------------------------------')
print(f'Respuestas correctas: {corrects}')
print(f'Respuestas incorrectas: {errors}\n')