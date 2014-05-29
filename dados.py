
from constantes import *
import random

class Dados(object):
	"""Implementa la logica de tirar los dados."""

	def __init__(self):
		"""Inicializacion del objeto."""
                self.valor_dados_atacantes = []
                self.valor_dados_defensores = []
		self.valor = 0
                self.ejercitos_atacantes_perdidos = 0
                self.ejercitos_defensores_perdidos = 0

	def __str__(self):
		"""Representacion de la configuracion de dados de la ultima
		tirada."""
                return str(self.valor)

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
                while (ejercitos_atacantes > 1) and (ejercitos_defensores > 0):
                    if (ejercitos_atacantes-1 >3):
                        agregar_dados(4, self.valor_dados_atacantes)
                    elif (ejercitos_defensores > 3):
                        agregar_dados(4, self.valor_dados_defensores)
                    agregar_dados(ejercitos_atacantes, self.valor_dados_atacantes)
                    agregar_dados(ejercitos_defensores,self.valor_dados_defensores)
                    
                

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
            self.valor =  random.randrange(1,7)
        
        def agregar_dados(self,cantidad_dados,ejercito):
            """Agrega los valores de los dados segun la cantidad de dados pasada por parametro, y se los agrega al ejercito"""
            for dado in xrange(1,cantidad_dados):
                ejercito.append(dame_numero_dado())
        
        def comparar_dados(self, otro):
            """Compara 2 dados si el primero es mayor devuelve true, si es igual o menor devuelve False. El primer dado corresponde al atacante y el segundo al defensor"""
            if self.valor > otro.valor:
                return True
            return False