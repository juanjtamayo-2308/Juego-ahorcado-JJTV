# Juego-ahorcado-JJTV
Diseño de codigo para juego del ahorcado con tres capas

#Nombre: Juan Tamayo

#Objetivo del sistema:
#Aplicar los conocimientos teóricos de la asignatura en la construcción de un sistema de software interactivo que emule las reglas del "Juego del Ahorcado".

#Descripcion de funcionalidades
#El sistema fue construido bajo una arquitectura de tres capas, lo que otorga separación e independencia a sus funciones:  
#Presentation Layer (Capa de Presentación): Funciona como la vía de comunicación directa entre el usuario y el sistema. A través de las funciones de "Interfaz" e "IntroducirLetra" , esta capa proporciona al usuario el estado de sus vidas y captura la letra que elige durante su turno.  
#Business Logic Layer (Capa de Lógica de Negocio): Actúa como el cerebro del sistema. Está compuesta por el "NucleoJuego" y se apoya en subprocesos clave: el "VerificadorLetra", encargado de comprobar la validez de la entrada del usuario , y el "GestorIntentos", responsable de contabilizar las vidas restantes del jugador.  
#Data Access Layer (Capa de Acceso a Datos): Sirve como estructura de apoyo para el sistema. En esta capa  se aloja y gestiona el banco de palabras de donde el software extrae al azar los términos utilizados en cada partida.  En cuanto a la usabilidad, el actor principal  ejecuta las acciones base de "Iniciar partida" y "Elegir letra". A partir de la elección de la letra, el sistema acciona procesos de inclusión para verificar si el carácter pertenece a la palabra , revelar su posición si es correcto, o actualizar el dibujo y mostrar los intentos si es incorrecto.  

#Fecha: 28.06.2026
