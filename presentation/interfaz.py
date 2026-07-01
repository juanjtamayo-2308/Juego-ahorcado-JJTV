#Imprime el texto en la consola y captura lo que dicte el usuario
#Juan Tamayo

from business_logic.motor_juego import MotorJuego

AHORCADO_DIBUJOS = [
    r"""
       +---+
       |   |
           |
           |
           |
           |
     =========
    """,
    r"""
       +---+
       |   |
       O   |
           |
           |
           |
     =========
    """,
    r"""
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
     =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
     =========
    """
]

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
  vidas_iniciales = motor.gestor_intentos.intentos_restantes
  
  print(f"Palabra asignada: {guiones_iniciales}")
  print(f"Vidas iniciales: {vidas_iniciales}")
  print("\n[Estructura base cargada con exito]")
  
  palabra_actual = guiones_iniciales
  
  while motor.gestor_intentos.tiene_intentos():
      print(f"\n======================================================")
      
      # Calculamos qué dibujo mostrar según las vidas perdidas
      intentos_fallados = vidas_iniciales - motor.gestor_intentos.intentos_restantes
      # Evitamos un error si fallan más veces de los dibujos que tenemos
      indice_dibujo = min(intentos_fallados, len(AHORCADO_DIBUJOS) - 1)
      print(AHORCADO_DIBUJOS[indice_dibujo])
      
      print(f"Palabra: {palabra_actual}")
      print(f"Vidas restantes: {motor.gestor_intentos.intentos_restantes}")
      
      letra = input("Introduce una letra (A-Z): ")
      
      try:
          resultado = motor.procesar_letra(letra)
          
          print(f"\n-> {resultado['Mensaje']}")
          palabra_actual = resultado['Palabra']
          
          if resultado.get("gano"):
              print(f"\n******************************************************")
              print(f"¡FELICIDADES! Ganaste. La palabra era: {motor.palabra_secreta}")
              print(f"******************************************************")
              break
              
          if resultado.get("perdio"):
              print(f"\n======================================================")
              print(AHORCADO_DIBUJOS[-1]) # Mostramos el dibujo completo al perder
              print(f"¡GAME OVER! Te quedaste sin vidas.")
              print(f"La palabra secreta era: {motor.palabra_secreta}")
              print(f"======================================================")
              break
              
      except ValueError as e:
          print(f"\n[ALERTA] {e}")

if __name__ == "__main__":
  ejecutar_juego() 
