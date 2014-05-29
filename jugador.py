
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
			while bobon == Interfaz.BOTON_IZQUIERDO and (tablero.color_pais(atacante) != self.color or tablero.ejercitos_pais(atacante) == 1):
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
		cuales 7 tienen que estar obligatoriamente en Asia.
		Un ejemplo de retorno de la funcion podria ser
		{"Zaire": 4, "Italia": 1}."""
		raise NotImplementedError()

	def reagrupar(self, tablero):
		"""Recibe el tablero y le pide al jugador que seleccione todos
		los ejercitos que desea reagrupar. Devuelve una lista de
		reagrupamientos.
		Solo se podran reagrupar ejercitos a paises limitrofes, nunca
		un pais podra quedar vacio.
		Un ejemplo de devolcion de esta funcion puede ser:
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
		raise NotImplementedError()

	def __str__(self):
		"""Representacion de un jugador."""
		return '%s (%s)' % (self.nombre, NOMBRE_COLORES[self.color])
