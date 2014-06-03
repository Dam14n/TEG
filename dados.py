
from constantes import *
import random

class Dados(object):
	"""Implementa la logica de tirar los dados."""

	def __init__(self):
		"""Inicializacion del objeto."""
		self.valor_dados_atacantes = []
		self.valor_dados_defensores = []
		self.ejercitos_atacantes_perdidos = 0
		self.ejercitos_defensores_perdidos = 0

	def __str__(self):
		"""Representacion de la configuracion de dados de la ultima
		tirada."""
		return str("Dados defensores: %s \nDados atacantes: %s") % (str(self.valor_dados_defensores),str(self.valor_dados_atacantes))

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
		ejercitos_atacantes = ejercitos_atacante
		ejercitos_defensores = ejercitos_atacado
		if (ejercitos_atacantes-1 >=3):
                    self.agregar_dados(3, self.valor_dados_atacantes)
                    if (ejercitos_defensores >= 3):
			self.agregar_dados(3, self.valor_dados_defensores)
                    elif (ejercitos_defensores <= 3):
			self.agregar_dados(ejercitos_defensores, self.valor_dados_defensores)
		elif (ejercitos_atacantes-1 <= 3):
                    self.agregar_dados(ejercitos_atacantes-1, self.valor_dados_atacantes)
                    if (ejercitos_defensores <= 3):
			self.agregar_dados(ejercitos_defensores, self.valor_dados_defensores)
                    elif (ejercitos_defensores >= 3): 
			self.agregar_dados(3, self.valor_dados_defensores)
		else:
			print "No se posee la cantidad de ejercitos necesarios."
			return
		self.comparar_dados(self.valor_dados_atacantes,self.valor_dados_defensores)             
	 
	def agregar_dados(self, cantidad_dados,ejercito):
		"""Agrega los valores de los dados segun la cantidad de dados pasada por parametro, y se los agrega al ejercito y los ordena de mayor a menor"""
		for valor in xrange(1,cantidad_dados+1):
			ejercito.append(self.dame_numero_dado())
		ejercito.sort(None,None,True)
            
	def ejercitos_perdidos_atacante(self):
		"""Devuelve la cantidad de ejercitos que perdio el atacante en
		la ultima tirada de dados."""
		return self.ejercitos_atacantes_perdidos

	def ejercitos_perdidos_atacado(self):
		"""Devuelve la cantidad de ejercitos que perdio el atacado en
		la ultima tirada de dados."""
		return self.ejercitos_defensores_perdidos
            
	def dame_numero_dado(self):
		"""Elige un numero aleatorio entre 1 y 6, para darle un valor al dado"""
		return random.randrange(1,7)
        
	def comparar_dados(self, ejercitos_atacantes, ejercitos_defensores):
		"""Genera la batalla de los ejercitos en donde se pasan como parametro dos listas con los valores de cada ejercito defensore y atacante respectivamentes y 
		se calcula quien perdio y gano cada batalla"""
		posicion = 0
		try:
			for atacante in ejercitos_atacantes:
				if atacante > ejercitos_defensores[posicion]:
					self.ejercitos_defensores_perdidos += 1
				else:
					self.ejercitos_atacantes_perdidos += 1
				posicion += 1
		except IndexError:
			return IndexError
        
	def dados_tirados_de_mas(self):
		"""Recibe las tiradas de los dados y se comprueba que la cantidad de dados de los defensores y atacantes sea menor que 3 en caso contrario se remueven los dados de menor valor"""
		while len(self.valor_dados_atacantes) > 3 or len(self.valor_dados_defensores) > 3:
			if len(self.valor_dados_atacantes) > len(self.valor_dados_defensores):
				self.valor_dados_atacantes.pop()
			elif len(self.valor_dados_atacantes) < len(self.valor_dados_defensores): 
				self.valor_dados_defensores.pop()