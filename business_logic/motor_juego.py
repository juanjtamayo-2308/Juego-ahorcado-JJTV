#Es la parte que enlaza las diferentes estructuras
from data_access.palabra_azar import seleccionar_palabra_azar
from business_logic.contador_vidas import GestorIntentos
from business_logic.verificador import caracter_valido

class MotorJuego:
  def __init__ (self):
    self.palabra_secreta = ""
    self.letras_adivinadas = []
    self.gestor_intentos = GestorIntentos()

  def iniciar_nueva_partida(self):
    self.palabra_secreta = seleccionar_palabra_azar().upper()
    self.letras_adivinadas = []
    self.gestor_intentos = GestorIntentos()
    return self.obtener_estado_palabra()

  def obtener_estado_palabra(self):
      resultado = ""
      for letra in self.palabra_secreta:
        if letra in self.letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
      return resultado.strip()

  def procesar_letra(self, letra):
      letra = letra.upper()
    
      if not caracter_valido(letra):
          raise ValueError("Error. Ingrese unicamente una letra de la A a la Z")

      if letra in self.letras_adivinadas:
        return {
            "Status": "Repetida",
            "Mensaje": f"Ya habias elegido esa letra '{letra}'.",
            "Palabra": self.obtener_estado_palabra()
        }

      self.letras_adivinadas.append(letra)
  
      if letra in self.palabra_secreta:
          gano = all(l in self.letras_adivinadas for l in self.palabra_secreta)
          return {
              "Status": "Acertaste",
              "Mensaje": f"Felicidades. La letra '{letra}' es correcta.",
              "Palabra": self.obtener_estado_palabra(),
              "gano": gano
          }
      else:
          self.gestor_intentos.restar_intento()
          perdio = not self.gestor_intentos.tiene_intentos()
          return {
              "Status": "Fallaste",
              "Mensaje": f"Incorrecto. La letra '{letra}' no pertenece a la palabra.",
              "Palabra": self.obtener_estado_palabra(),
              "perdio": perdio
          }

  

  def procesar_letra(self, letra):
    pass
