
from constantes import *

class Tarjeta(object):
	"""Implementacion de una tarjeta de pais."""

	def __init__(self, pais, tipo):
		"""Constructor desde pais y tipo."""
		self.pais = pais
		self.tipo = tipo

	def __str__(self):
		"""Representacion grafica."""
		return "(%s, %s)" % (self.pais, NOMBRE_TARJETAS[self.tipo])

class Mazo(object):
	"""Implementacion del mazo de tarjetas de pais."""

	def __init__(self, paises_por_tarjeta):
		"""Creacion desde un diccionario de paises segun tipo.
		Debe inicializar el mazo con todas las tarjetas mezcladas."""
		raise NotImplementedError()

	def sacar_tarjeta(self):
		"""Saca una tarjeta del mazo.
		Si el mazo se acabara, debe mezclar y empezar a repartir desde
		las tarjetas ya devueltas."""
		raise NotImplementedError()

	def devolver_tarjeta(self, tarjeta):
		"""Recibe una tarjeta y la guarda en el pilon de tarjetas
		devueltas. Cuando se acaben las tarjetas del mazo, se mezclaran
		las ya devueltas."""
		raise NotImplementedError()

	def cantidad_tarjetas(self):
		"""Devuelve la cantidad *total* de tarjetas (tanto en el mazo
		como devueltas)."""
		raise NotImplementedError()

