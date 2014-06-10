
from constantes import *
from random import shuffle

class Tarjeta(object):
	"""Implementacion de una tarjeta de pais."""

	def __init__(self, pais, tipo):
		"""Constructor desde pais y tipo."""
		self.pais = pais
		self.tipo = tipo
		self.canje = True

	def __str__(self):
		"""Representacion grafica."""
		return "(%s, %s)" % (self.pais, NOMBRE_TARJETAS[self.tipo])
        
        def tipo(self):
            """Devuelve el tipo de tarjeta"""
            return self.tipo

class Mazo(object):
	"""Implementacion del mazo de tarjetas de pais."""

	def __init__(self, paises_por_tarjeta):
		"""Creacion desde un diccionario de paises segun tipo.
		Debe inicializar el mazo con todas las tarjetas mezcladas."""
		self.cantidad = 0
		self.tarjetas_a_pedir = []
		self.tarjetas_devueltas = []
		self.llenar_mazo(paises_por_tarjeta)

	def __len__(self):
		"""Devuelve un numero entero que representa el numero de tarjetas total en el mazo."""
		return len(self.tarjetas_a_pedir) + len(self.tarjetas_devueltas)
		
	def llenar_mazo(self, paises_por_tarjeta):
		"""Recibe un diccionario con los paises y tipo de tarjeta.
		Crea objetos de la clase Tarjeta con los datos del diccionario.
		Tambien crea una lista vacia y agrega todas las Tarjetas. Luego llama a mezclar_mazo para mezclarlas."""
		tarjetas = []
		for tipo in paises_por_tarjeta:
			for pais in paises_por_tarjeta[tipo]:	
				tarjetas.append(Tarjeta(pais, tipo))
		self.mezclar_mazo(tarjetas)
		
	def mezclar_mazo(self, tarjetas):
		"""Recibe una lista de tarjetas(ver clase Tarjeta).
		Mezcla las tarjetas en el atributo tarjetas_a_pedir."""
		try:
			while True:
				self.tarjetas_a_pedir.append(tarjetas.pop())
		except IndexError:
			shuffle(self.tarjetas_a_pedir)

	def sacar_tarjeta(self):
		"""Saca una tarjeta del mazo.
		Si el mazo se acabara, debe mezclar y empezar a repartir desde
		las tarjetas ya devueltas."""
		try:
			tarjeta = self.tarjetas_a_pedir.pop()
		except IndexError:
			self.mezclar_mazo(self.tarjetas_devueltas)
			tarjeta = self.tarjetas_a_pedir.pop()
		return tarjeta

	def devolver_tarjeta(self, tarjeta):
		"""Recibe una tarjeta y la guarda en el pilon de tarjetas
		devueltas. Cuando se acaben las tarjetas del mazo, se mezclaran
		las ya devueltas."""
		self.tarjetas_devueltas.append(tarjeta)

	def cantidad_tarjetas(self):
		"""Devuelve la cantidad *total* de tarjetas (tanto en el mazo
		como devueltas)."""
		return len(self)