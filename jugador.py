
from interfaz import Interfaz
from constantes import *

class Jugador(object):
	"""Representa a un jugador de TEG."""
	def __init__(self, color, nombre):
		"""Crea un jugador desde un color y un nombre."""
		self.color = color
		self.nombre = nombre

	def atacar(self, tablero):
		"""Le pide al usuario que ingrese un par de paises para
		realizar un ataque. Devuelve None si el jugador no quiere
		atacar y un par (atacante, atacado) en caso contrario."""
		while True:
			Interfaz.setear_titulo('%s ataca. Seleccionar atacante' % self)

			atacante, boton = Interfaz.seleccionar_pais()
			while boton == Interfaz.BOTON_IZQUIERDO and (tablero.color_pais(atacante) != self.color or tablero.ejercitos_pais(atacante) == 1):
				atacante, boton = Interfaz.seleccionar_pais()
			if boton != Interfaz.BOTON_IZQUIERDO:
				return None

			Interfaz.setear_titulo('%s ataca. Seleccionar pais atacado por %s' % (self, atacante))

			atacado, boton = Interfaz.seleccionar_pais()
			while boton == Interfaz.BOTON_IZQUIERDO and (tablero.color_pais(atacado) == self.color or not tablero.es_limitrofe(atacante, atacado)):
				atacado, boton = Interfaz.seleccionar_pais()
			if boton != Interfaz.BOTON_IZQUIERDO:
				continue
			return (atacante, atacado)

	def agregar_ejercitos(self, tablero, cantidad):
		"""Recibe un tablero y un diccionario con la cantidad de paises
		a poner. Devuelve un diccionario con los paises que el usuario
		selecciono.
		Por ejemplo, si cantidad = {"": 2, "Africa": 3}, eso significa
		que el jugador va a poner 5 ejercitos en sus paises, de los
		cuales 3 tienen que estar obligatoriamente en Africa.
		Un ejemplo de retorno de la funcion podria ser
		{"Zaire": 4, "Italia": 1}."""
		entrar = True
		asignaciones = {}
		while entrar:
			elegido = self.pedir_pais_propio("%s en etapa de asignacion. Seleccionar pais." % self)
			while elegido and not (cantidad[""] or cantidad[tablero.continente_pais(elegido)]):
				elegido = self.pedir_pais_propio("%s en etapa de asignacion. Seleccionar pais." % self)
			
			if elegido:
				if cantidad.has_key(tablero.continente_pais(elegido)):
					cantidad[tablero.continente_pais(elegido)] -= 1
				else: cantidad[""] -= 1
			
				
				
				
			
			else: entrar = not entrar
		return asignaciones

	def reagrupar(self, tablero):
		"""Recibe el tablero y le pide al jugador que seleccione todos
		los ejercitos que desea reagrupar. Devuelve una lista de
		reagrupamientos.
		Solo se podran reagrupar ejercitos a paises limitrofes, nunca
		un pais podra quedar vacio.
		Un ejemplo de devolucion de esta funcion puede ser:
		[('Argentina', 'Uruguay', 2), ('Argentina', 'Brasil', 1),
			('Chile', 'Argentina', 1)]
		Esto significa que de Argentina se reagrupan 3 ejercitos, 2 con
		destino a Uruguay y 1 con destino a Brasil. Argentina tiene que
		tener al menos 4 ejercitos. De Chile se pasa uno a Argentina,
		por lo que Chile tiene que tener al menos 1. Todos los paises
		tienen que pertenecer al jugador. Despues de implementado el
		reagrupamiento, Brasil quedara con 1 ejercito mas, Uruguay con
		2 mas, Argentina con 2 menos (salen 3, entra 1) y Chile con 1
		menos."""
		entrar = True
		reagrupamientos = []
		while entrar:
			origen = self.pedir_pais_propio()
			while origen and tablero.ejercitos_pais(origen) > 1:
				origen = self.pedir_pais_propio("%s en etapa de reagrupamiento. Seleccionar pais de origen." % self)
			if origen:
				cantidad_a_mover = self.listar_opciones(tablero, origen, "Reagrupamiento")
				destino = pedir_pais_propio('%s esta reagrupando. Seleccionar pais de destino.' % self)
				while destino and not tablero.es_limitrofe(origen, destino):
					destino = pedir_pais_propio('%s esta reagrupando. Seleccionar pais de destino.' % self)
				if not destino: continue
				reagrupamientos += (origen, destino, cantidad_a_mover)
				tablero.actualizar_interfaz({origen: - cantidad_a_mover, destino: cantidad_a_mover})
				tablero.asignar_ejercitos(origen, - cantidad_a_mover)
				tablero.asignar_ejercitos(destino, cantidad_a_mover)
			else: entrar = not entrar
		return reagrupamientos
		
	def listar_opciones(self, tablero, pais, mensaje):
		""""""
		numero_ejercitos = tablero.ejercitos_pais(pais)
		# Creo la lista desde 1 hasta uno menos de la cantidad de ejercitos en el pais(debe haber al menos un ejercito).
		opciones_ejercitos = [cantidad for cantidad in xrange(numero_ejercitos - 1) if cantidad]
		return Interfaz.elegir(mensaje, "Ejercitos del pais %s." % pais, opciones_ejercitos)
		
	def pedir_pais_propio(self, mensaje):
		""""""
		Interfaz.setear_titulo(mensaje)
		origen, boton = Interfaz.seleccionar_pais()
		while boton == Interfaz.BOTON_IZQUIERDO and tablero.color_pais(origen) != self.color:
			origen, boton = Interfaz.seleccionar_pais()
		if boton != Interfaz.BOTON_IZQUIERDO:
			return None
		return origen
	
	def su_color(self):
		""""""
		return self.color
		
	def su_nombre(self):
		""""""
		return self.nombre
		
	def __str__(self):
		"""Representacion de un jugador."""
		return '%s (%s)' % (self.nombre, NOMBRE_COLORES[self.color])
