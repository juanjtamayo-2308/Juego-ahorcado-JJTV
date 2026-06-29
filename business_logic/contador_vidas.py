#Controla los intentos del usuario
#Juan Tamayo

class GestorIntentos:
  def init(self,limite_vidas=5):
      self.intentos_restantes = limite_vidas
    def resta_intento(self):
      if self.intentos_restantes > 0:
        self.intentos_restantes -= 1
        return self.intentos_restantes
      def vidas(self):
        return self.intentos_restantes > 0
        
