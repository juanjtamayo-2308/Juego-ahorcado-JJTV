#Es la parte que enlaza las diferentes estructuras
from data_access.palabra_azar import seleccionar_palabra_azar
from business_logic.contador_vidas import GestorIntentos

class MotorJuego:
  def __init__ (self):
    self.palabra_secreta = ""
    self.letras_adivinadas = []
    self.gestor_intentos = GestorIntentos()

  def iniciar_nueva_partida(self):
    self.palabra_secreta = seleccionar_palabra_azar()
    self.letras_adivinadas = []
    self.gestor_intentos = GestorIntentos()
    return "_" * len(self.palabra_secreta)

  def procesar_letra(self, letra):
    pass
