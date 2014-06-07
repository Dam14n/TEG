
from constantes import *
from interfaz import Interfaz

class _Pais(object):
	""""""
	def __init__(self, nombre, continente, limitrofes):
		""""""
		self.nombre = nombre
		self.limitrofes = limitrofes
		self.color = None
		self.ejercitos = None
		self.continente = continente

	def su_nombre(self):
		""""""
		return self.nombre
		
	def su_color(self):
		""""""
		return self.color
	
	def su_continente(self):
		""""""
		return self.continente
		
	def sus_ejercitos(self):
		""""""
		return self.ejercitos
	
	def sus_limitrofes(self):
		""""""
		return self.limitrofes

	def ocupar(self, color, ejercitos):
		""""""
		self.color = color
		self.ejercitos = ejercitos
	
	def asignar_ejercitos(self, ejercitos):
		""""""
		self.ejercitos = ejercitos

class Tablero(object):
	"""Clase que representa el tablero de juego."""

	def __init__(self, continentes, limitrofes):
		"""Crea un tablero desde un diccionario de continentes con su
		lista de paises, y un diccionario de paises y su lista de
		limitrofes."""
		self.paises = {}
		self.continentes = {}
		for continente in continentes:
			self.continentes[continente] = len(continentes[continente])
			for pais in continentes[continente]:
				self.paises[pais] = _Pais(pais, continente, limitrofes[pais])

	def ocupar_pais(self, pais, color, ejercitos = 1):
		"""Ocupa el pais indicado con ejercitos del color."""
		self.paises[pais].ocupar(color, ejercitos)

	def asignar_ejercitos(self, pais, ejercitos):
		"""Suma o resta una cantidad de ejercitos en el pais indicado."""
		self.paises[pais].asignar_ejercitos(ejercitos)

	def actualizar_interfaz(self, agregados = None):
		"""Redibuja interfaz grafica. Puede recibir un diccionario de
		paises y numero de ejercitos que se adicionan o sustraen a los
		que estan ubicados en el tablero.
		Por ejemplo, si el diccionario fuera
		{'Argentina': -1, 'Brasil': 1}, el tablero se dibujaria con un
		ejercito menos en Argentina y uno mas en Brasil."""
		paises = {}
		for pais in agregados:
			paises[pais] = (self.paises[pais].su_color(), agregados[pais])
		return Interfaz.ubicar_ejercitos(paises)
		# Utilizar la funcion de la Interfaz, que recibe un diccionario
		# de paises y colores, por ejemplo:
		# >>> paises = {'Argentina': (COLOR_NEGRO, 10), 'Brasil':
		# ...	(COLOR_ROSA, 1)}
		# >>> Interfaz.ubicar_ejercitos(paises)
		# Va a poner 10 ejercitos negros en Argentina y 1 rosa en
		# Brasil.

	def color_pais(self, pais):
		"""Devuelve el color de un pais."""
		return self.paises[pais].su_color()

	def ejercitos_pais(self, pais):
		"""Devuelve la cantidad ejercitos en un pais."""
		return self.paises[pais].sus_ejercitos()

	def es_limitrofe(self, pais1, pais2):
		"""Informa si dos paises son limitrofes."""
		return pais2 in self.paises[pais1].sus_limitrofes()

	def cantidad_paises(self):
		"""Informa la cantidad de paises totales."""
		# preguntar que sentido tiene este metodo.
		return len(self.paises.values())

	def cantidad_paises_continente(self, continente):
		"""Informa la cantidad de paises en continente."""
		#Este igual.
		return len(self.continentes[continente])

	def continente_pais(self, pais):
		"""Informa el continente de un pais."""
		return self.paises[pais].su_continente()

	def paises_color(self, color):
		"""Devuelve la lista de paises con ejercitos del color."""
		paises_del_color = []
		for pais in self.paises.values():
			if pais.su_color() == color: paises_del_color.append(pais)
		return paises_del_color
