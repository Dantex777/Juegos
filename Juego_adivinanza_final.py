from operator import truediv
import random

#funcion que compara si el numero es mayor, menor o igual al del sistema
def compara(numero_aleatorio, numero_elegido):
  
  if numero_elegido < numero_aleatorio:
      print("Busca un número más grande!!!")      
      return False       
        
  if numero_elegido > numero_aleatorio:         
      print("Busca un número más pequeño!!!")
      return False
      
  if numero_aleatorio == numero_elegido:
      print("GANASTE!!!")
      return True



#Funcion que inicia el juego
def run():
    vidas = 5
    numero_aleatorio = random.randint(1, 10)
    numero_elegido = int (input("""**************************************************
    Elige un número del 1 al 10: 
**************************************************"""))
    while vidas >0 and numero_aleatorio != numero_elegido:
      compara(numero_aleatorio, numero_elegido)
      print("Tienes: " + str(vidas) + " Vidas")
      numero_elegido = int(input("Elige otro número: "))
      vidas -= 1
    if compara(numero_aleatorio, numero_elegido) == False:
      print("Perdiste Totalmente")

    else:
      print("""*****************
***Lo lograste***
*****************""")

if __name__ == '__main__' :
    run()