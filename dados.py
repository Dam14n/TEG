
from constantes import *
import random

class Dados(object):
	"""Implementa la logica de tirar los dados."""

	def __init__(self):
		"""Inicializacion del objeto."""
		self.dados_atacante = []
		self.dados_atacado = []
		self.cantidad_atacante = 0
		self.cantidad_atacado = 0
		self.ejercitos_atacantes_perdidos = 0
		self.ejercitos_atacados_perdidos = 0

	def __str__(self):
		"""Representacion de la configuracion de dados de la ultima
		tirada."""
		#Aca pase de tener lista a cadena, Ejemplo:
		# de [2,3,4] pasa a "2 - 3 - 4"
		# me parece mejor.. un cambio simple.
		atacante = " - ".join([str(x) for x in self.dados_atacante])
		atacado = " - ".join([str(x) for x in self.dados_atacado])
		return "Dados del atacado: %s \nDados del atacante: %s" % (atacado, atacante)

	def lanzar_dados(self, ejercitos_atacante, ejercitos_atacado):
		"""Recibe la cantidad de ejercitos presentes en el pais
		atacante y en el pais atacado. Realiza la tirada de los dados.
		El pais que ataca tiene que tener al menos dos ejercitos.
		El pais que ataca ataca con hasta un dado menos que los
		ejercitos que posee, mientras que el pais que defiende lo
		hace hasta con tantos dados como ejercitos.
		La cantidad maxima de dados con la que un pais ataca o defiende
		es siempre 3.
		Cada jugador tira sus dados.
		Los mismos se ordenan de mayor a menor.
		Si un jugador tiro mas dados que otro, los de menor valor se
		descartan.
		Se comparan uno a uno los dados ordenados.
		Cuando el valor de un dado atacante fuera *mayor* que el del
		atacado, el atacado pierde un ejercito. Si no, el atacante lo
		pierde.
		(Leer el reglamento del juego.)"""
		self.reiniciar()
		if ejercitos_atacante > 3: self.cantidad_atacante = 3
		else: self.cantidad_atacante = ejercitos_atacante - 1
		if not self.cantidad_atacante: return # Significa que ejercitos_atacante es 1
		if ejercitos_atacado > 2: self.cantidad_atacado = 3
		else: self.cantidad_atacado = ejercitos_atacado
		self.agregar_dados()
		self.comparar_dados()

	def reiniciar(self):
		"""Reinicializa el dado con los contadores en cero."""
		self.dados_atacante = []
		self.dados_atacado = []
		self.ejercitos_atacantes_perdidos = 0
		self.ejercitos_atacados_perdidos = 0

	def agregar_dados(self):
		"""Agrega los valores de los dados segun la cantidad
		de dados pasada por parametro, y se los agrega al
		ejercito y los ordena de mayor a menor."""
		for cantidad_dados, dados in ((self.cantidad_atacante, self.dados_atacante ), (self.cantidad_atacado,self.dados_atacado)):
			for i in xrange(cantidad_dados):
                            dados.append(random.randrange(1,7))
			dados.sort(None, None, True)

	def ejercitos_perdidos_atacante(self):
		"""Devuelve la cantidad de ejercitos que perdio el atacante en
		la ultima tirada de dados."""
		return self.ejercitos_atacantes_perdidos

	def ejercitos_perdidos_atacado(self):
		"""Devuelve la cantidad de ejercitos que perdio el atacado en
		la ultima tirada de dados."""
		return self.ejercitos_atacados_perdidos

	def comparar_dados(self):
		"""Compara la tirada de dados de ambos jugadores."""
		posicion = 0
		try:
			for atacante in self.dados_atacante:
				if atacante > self.dados_atacado[posicion]:
					self.ejercitos_atacados_perdidos += 1
				else:
					self.ejercitos_atacantes_perdidos += 1
				posicion += 1
		except IndexError:
			pass
