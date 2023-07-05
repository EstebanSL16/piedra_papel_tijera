import random

base = ('piedra', 'papel', 'tijera')
print("Juego de Piedra, Papel o Tijera\n")
#base = random.sample(base, len(base))
#computer = base[1]
contUser = []
contComputer = []
for i in range(3):
  computer = random.choice(base)
  user = input("piedra, papel o tijera => ")
  user = user.lower()
  print("Opcion escogida por la maquina: ", computer)

  if user == computer:
    print('Empate!\n')
  elif user == 'piedra':
    if computer == 'papel':
      print('papel gana a piedra')
      print('pierdes!\n')
      contComputer.append(1)
    else:
      print('piedra gana a tijera')
      print('ganaste!\n')
      contUser.append(1)
  elif user == 'papel':
    if computer == 'tijera':
      print('tijera gana a papel')
      print('pierdes!\n')
      contComputer.append(1)
    else:
      print('papel gana a piedra')
      print('ganaste!\n')
      contUser.append(1)
  elif user == 'tijera':
    if computer == 'piedra':
      print('piedra gana a tijera')
      print('pierdes!\n')
      contComputer.append(1)
    else:
      print('tijera gana a papel')
      print('ganaste!\n')
      contUser.append(1)

if len(contUser) > len(contComputer):
  print("¡Gana el usuario!")
elif len(contUser) == len(contComputer):
  print("¡Empate!")
else:
  print("¡Gana la Maquina!")

