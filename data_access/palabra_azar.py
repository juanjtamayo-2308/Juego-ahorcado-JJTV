#Codigo para generar palabra al azar del banco de palabras
#Juan Tamayo

import random
from data_access.bnco_palabras import obtener_list_words

def seleccionar_palabra_azar():
  palabras = obtener_list_words()
  return random.choice(palabras)
  
