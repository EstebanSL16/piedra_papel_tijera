import random

base = ('piedra', 'papel', 'tijera')
base = random.sample(base, len(base))
print(base)
#print(type(base))
computer = base[1]

user = input("piedra, papel o tijera => ")
user = user.lower()
print("la opcion de la maquina", computer)

if user == computer:
  print('Empate!')
elif user == 'piedra':
  if computer == 'papel':
    print('papel gana a piedra')
    print('pierdes!')
  else:
    print('piedra gana a tijera')
    print('ganaste!')
elif user == 'papel':
  if computer == 'tijera':
    print('tijera gana a papel')
    print('pierdes!')
  else:
    print('papel gana a piedra')
    print('ganaste!')
elif user == 'tijera':
  if computer == 'piedra':
    print('piedra gana a tijera')
    print('pierdes!')
  else:
    print('tijera gana a papel')
    print('ganaste!')

