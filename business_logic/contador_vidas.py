#Controla los intentos del usuario
#Juan Tamayo

class GestorIntentos:
  def __init__(self,limite_vidas=5):
      self.intentos_restantes = limite_vidas
    
  def resta_intento(self):
      if self.intentos_restantes > 0:
        self.intentos_restantes -= 1
      return self.intentos_restantes
        
  def tiene_intentos(self):
      return self.intentos_restantes > 0
        
