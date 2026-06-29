#Codigo para verificar ingreso de letra (A-Z)

def caracter_valido(caracter):
  if len(caracter) != 1:
    return False
  return caracter.isalpha()
  
