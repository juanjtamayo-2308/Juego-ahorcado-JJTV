#Imprime el texto en la consola y captura lo que dicte el usuario
#Juan Tamayo

from business_logic.motor_juego import MotorJuego

def mostrar_pantalla_inicial():
  print("******************************************************")
  print("******************************************************")
  print("                 JUEGO DEL AHORCADO                   ")
  print("               Created by Juan Tamayo                 ")
  print("           UIDE - LOGICA DE PROGRAMACION              ")
  print("******************************************************")
  print("******************************************************")

def ejecutar_juego():
  motor = MotorJuego()
  mostrar_pantalla_inicial()

  guiones_iniciales = motor.iniciar_nueva_partida()
  print(f"Palabra asignada por DAL: {guiones_iniciales}")
  print(f"Vidas iniciales por BLL: {motor.gestor_intentos.intentos_restantes}")
  print("\n[Estructura base cargada con exito]")

if __name__ == "__main__":
  ejecutar_juego()
  
