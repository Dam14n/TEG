
from constantes import *
from interfaz import Interfaz

class Tablero(object):
	"""Clase que representa el tablero de juego."""

	def __init__(self, continentes, limitrofes):
		"""Crea un tablero desde un diccionario de continentes con su
		lista de paises, y un diccionario de paises y su lista de
		limitrofes."""
		raise NotImplementedError()

	def ocupar_pais(self, pais, color, ejercitos=1):
		"""Ocupa el pais indicado con ejercitos del color."""
		raise NotImplementedError()

	def asignar_ejercitos(self, pais, ejercitos):
		"""Suma o resta una cantidad de ejercitos en el pais indicado."""
		raise NotImplementedError()

	def actualizar_interfaz(self, agregados=None):
		"""Redibuja interfaz grafica. Puede recibir un diccionario de
		paises y numero de ejercitos que se adicionan o sustraen a los
		que estan ubicados en el tablero.
		Por ejemplo, si el diccionario fuera
		{'Argentina': -1, 'Brasil': 1}, el tablero se dibujaria con un
		ejercito menos en Argentina y uno mas en Brasil."""
		raise NotImplementedError()
		# Utilizar la funcion de la Interfaz, que recibe un diccionario
		# de paises y colores, por ejemplo:
		# >>> paises = {'Argentina': (COLOR_NEGRO, 10), 'Brasil':
		# ...	(COLOR_ROSA, 1)}
		# >>> Interfaz.ubicar_ejercitos(paises)
		# Va a poner 10 ejercitos negros en Argentina y 1 rosa en
		# Brasil.

	def color_pais(self, pais):
		"""Devuelve el color de un pais."""
		raise NotImplementedError()

	def ejercitos_pais(self, pais):
		"""Devuelve la cantidad ejercitos en un pais."""
		raise NotImplementedError()

	def es_limitrofe(self, pais1, pais2):
		"""Informa si dos paises son limitrofes."""
		raise NotImplementedError()

	def cantidad_paises(self):
		"""Informa la cantidad de paises totales."""
		raise NotImplementedError()

	def cantidad_paises_continente(self, continente):
		"""Informa la cantidad de paises en continente."""
		raise NotImplementedError()

	def continente_pais(self, pais):
		"""Informa el continente de un pais."""
		raise NotImplementedError()

	def paises_color(self, color):
		"""Devuelve la lista de paises con ejercitos del color."""
		raise NotImplementedError()

