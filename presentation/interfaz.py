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
  print(f"Palabra asignada: {guiones_iniciales}")
  print(f"Vidas iniciales: {motor.gestor_intentos.intentos_restantes}")
  print("\n[Estructura base cargada con exito]")
  
  # --- AQUÍ INICIA EL CICLO DE JUEGO INTERACTIVO ---
  palabra_actual = guiones_iniciales
  
  # Mientras el gestor de intentos diga que tenemos vidas, el juego sigue
  while motor.gestor_intentos.tiene_intentos():
      print(f"\n======================================================")
      print(f"Palabra: {palabra_actual}")
      print(f"Vidas restantes: {motor.gestor_intentos.intentos_restantes}")
      
      # Capturamos la letra introducida por el usuario
      letra = input("Introduce una letra (A-Z): ")
      
      try:
          # Enviamos la letra a la lógica de negocio para procesarla
          resultado = motor.procesar_letra(letra)
          
          print(f"\n-> {resultado['Mensaje']}")
          palabra_actual = resultado['Palabra']
          
          # Verificamos si ya ganó
          if resultado.get("gano"):
              print(f"\n******************************************************")
              print(f"¡FELICIDADES! Ganaste. La palabra era: {motor.palabra_secreta}")
              print(f"******************************************************")
              break
              
          # Verificamos si se quedó sin vidas
          if resultado.get("perdio"):
              print(f"\n======================================================")
              print(f"¡GAME OVER! Te quedaste sin vidas.")
              print(f"La palabra secreta era: {motor.palabra_secreta}")
              print(f"======================================================")
              break
              
      except ValueError as e:
          # Si el usuario mete un número o caracter inválido, atrapamos el error aquí
          print(f"\n[ALERTA] {e}")

if __name__ == "__main__":
  ejecutar_juego()
  
