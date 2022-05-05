import time

status = "desligado"

while ( status == "desligado" ):
  opcao = input( "Digite ligar para ativar imãs e sensor: " )
  if ( opcao != "ligar" ):
    status = "desligado"
  else:
    status = "ligado"

print ("Imâs ligados. O Sensor identificou 68°")

angulo = 68

def puxar (angulo):
  if (angulo > 58):
    angulo = angulo - 2
    print('Estou muito longe do navio, só consigo puxar 2')
    time.sleep(2)
    print ("Faltam", angulo)
  elif(angulo > 10):
    angulo = angulo - 10
    print('Agora estou perto, consigo puxar 10')
    time.sleep(2)
    print ("Faltam", angulo)
  else:
    angulo = angulo - 1
    print ('Estou quase reto, irei diminuir minha força')
    time.sleep(1)
    print ("Faltam", angulo)


  return angulo  

while (angulo != 0):
  angulo = puxar(angulo)

print ("Desencalhei, agora posso continuar minha viagem")

while ( status == "ligado" ):
  opcao = input( "Digite desligar para desativar imãs: " )
  if ( opcao != "desligar" ):
    status = "ligado"
  else:
    status = "desligado"

print ("Imãs desativados")