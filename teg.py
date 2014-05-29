
import random
import time
import math

from constantes import *

from jugador import Jugador
from interfaz import Interfaz
from mazo import Mazo
from tablero import Tablero
from dados import Dados

# Tablero clasico:
import paises as paises
# Tablero de Argentina:
#import paises_argentina as paises

class TEG(object):
	"""Implementa la logica de una partida de TEG."""

	def __init__(self):
		"""Constructor de la clase.
		Inicializa la interfaz grafica y los objetos que va a utilizar
		durante el juego."""
		self.mazo = Mazo(paises.paises_por_tarjeta)
		self.dados = Dados()
		self.tablero = Tablero(paises.paises_por_continente, paises.paises_limitrofes)
		Interfaz.iniciar(paises.coordenadas_de_paises, paises.archivo_tablero, paises.color_tablero)

		self.jugadores = []

		# Eventualmente aca haya falta agregar mas cosas...

	def configurar_el_juego(self):
		"""Pone a los jugadores en el juego."""

		Interfaz.setear_titulo('Configurando el juego')
		n = Interfaz.elegir('Jugadores', 'Seleccione el numero de jugadores', range(2,7))

		nombre_colores = NOMBRE_COLORES.values()
		for i in range(n):
			nombre = Interfaz.elegir('Jugador %d' % (i + 1), 'Ingrese el nombre del jugador %d' % (i + 1))
			color = Interfaz.elegir('Jugador %d' % (i + 1), 'Ingrese el color del jugador %d' % (i + 1), nombre_colores)
			nombre_colores.remove(color)

			c = NOMBRE_COLORES.keys()[NOMBRE_COLORES.values().index(color)]
			self.jugadores.append(Jugador(c, nombre))

	def repartir_paises(self):
		"""Reparte en ronda las tarjetas de paises y pone un ejercito
		en cada uno de los paises."""

		Interfaz.setear_titulo('Repartiendo paises iniciales')

		ntarjetas = self.mazo.cantidad_tarjetas()
		njugadores = len(self.jugadores)

		for jugador in \
			self.jugadores * (ntarjetas / njugadores) + \
			random.sample(self.jugadores, ntarjetas % njugadores):
				t = self.mazo.sacar_tarjeta()
				self.tablero.ocupar_pais(t.pais, jugador.color, 1)
				self.mazo.devolver_tarjeta(t)

	def agregar_ejercitos_inicial(self, inicia_ronda):
		"""Realiza la primer fase de colocacion de ejercitos."""

		Interfaz.setear_titulo('Incorporando ejercitos')

		ejercitos_primera = int(math.ceil(self.tablero.cantidad_paises() / 10.0))
		ejercitos_segunda = int(math.ceil(self.tablero.cantidad_paises() / 20.0))

		for cantidad in (ejercitos_primera, ejercitos_segunda):
			for i in range(len(self.jugadores)):
				jugador = self.jugadores[(inicia_ronda + i) % len(self.jugadores)]

				Interfaz.alertar(jugador, '%s pone ejercitos' % jugador)

										# cantidad de ejercitos
										#en cualquier continente
				ejercitos = jugador.agregar_ejercitos(self.tablero, {"": cantidad})

				assert(sum(ejercitos.values()) == cantidad)
				for pais in ejercitos:
					assert(self.tablero.color_pais(pais) == jugador.color)
					self.tablero.asignar_ejercitos(pais, ejercitos[pais])

				self.tablero.actualizar_interfaz()

	def realizar_fase_ataque(self, jugador):
		"""Implementa la fase de ataque de un jugador.
		Sucesivamente hace combatir a los paises seleccionados.
		Devuelve el numero de paises conquistados."""

		Interfaz.setear_titulo('%s ataca' % jugador)
		Interfaz.alertar(jugador, '%s ataca' % jugador)

		paises_ganados = 0
		while True:
			ataque = jugador.atacar(self.tablero)
			if not ataque:
				break
			atacante, atacado = ataque

			assert(self.tablero.es_limitrofe(atacante, atacado))
			assert(self.tablero.ejercitos_pais(atacante) > 1)

			self.dados.lanzar_dados(self.tablero.ejercitos_pais(atacante), self.tablero.ejercitos_pais(atacado))
			self.tablero.asignar_ejercitos(atacante, -self.dados.ejercitos_perdidos_atacante())
			self.tablero.asignar_ejercitos(atacado, -self.dados.ejercitos_perdidos_atacado())

			Interfaz.setear_titulo('%s: -%d, %s: -%d %s' % (atacante, self.dados.ejercitos_perdidos_atacante(), atacado, self.dados.ejercitos_perdidos_atacado(), self.dados))

			if self.tablero.ejercitos_pais(atacado) == 0:
				paises_ganados += 1
				mover = Interfaz.elegir(jugador, 'Cuantos ejercitos se desplazan a %s?' % atacado, range(1, min(self.tablero.ejercitos_pais(atacante) - 1, 3) + 1))
				self.tablero.asignar_ejercitos(atacante, -mover)
				self.tablero.ocupar_pais(atacado, jugador.color, mover)

				self.tablero.actualizar_interfaz()
			else:
				self.tablero.actualizar_interfaz()
				time.sleep(1)

		return paises_ganados

	def realizar_fase_reagrupamiento(self, jugador):
		"""
		Realiza el reagrupamiento de ejercitos.
		"""

		Interfaz.setear_titulo('%s reagrupa' % jugador)
		Interfaz.alertar(jugador, '%s reagrupa' % jugador)

		lista = jugador.reagrupar(self.tablero)

		# Se fija que el reagrupamiento sea consistente:
		salientes = {}
		for origen, destino, cantidad in lista:
			assert(self.tablero.es_limitrofe(origen, destino))
			assert(self.tablero.color_pais(origen) == jugador.color)
			assert(self.tablero.color_pais(destino) == jugador.color)
			salientes[origen] = salientes.get(origen, 0) + cantidad
		for pais in salientes:
			assert(self.tablero.ejercitos_pais(pais) > salientes[pais])

		# Aplica la lista de cambios:
		for origen, destino, cantidad in lista:
			self.tablero.asignar_ejercitos(origen, -cantidad)
			self.tablero.asignar_ejercitos(destino, cantidad)

	def manejar_tarjetas(self, jugador, paises_ganados):
		"""
		Realiza la fase de obtencion de tarjetas de pais.
		1) Si el jugador gano un pais del cual no habia usado una
		tarjeta que posee, se colocan 2 ejercitos en ese pais.
		2) Si el jugador realizo menos de 3 canjes y gano al menos un
		pais o si realizo 3 o mas cajes y gano al menos dos paises,
		recibe una nueva tarjeta de pais.
		3) Si recibio tarjeta de pais y posee ese pais, recibe 2
		ejercitos adicionales en el mismo.
		"""
		raise NotImplementedError()

	def agregar_ejercitos(self, inicia_ronda):
		"""Realiza la fase general de colocacion de ejercitos.
		La cantidad de ejercitos a agregar son:
		1) Si el jugador tiene tres tarjetas con el mismo simbolo o si
		tiene tres tarjetas con distinto simbolo, entonces se realizara
		el canje. Cuando se realiza el canje, las tarjetas del jugador
		se devuelven al mazo.
		El primer canje otorgara 4 ejercitos adicionales para ser
		colocados en cualquier pais, el segundo 7, el tercero 10 y a
		partir de ahi 15, 20, 25, etc.
		2) El jugador agregara tantos ejercitos como paises / 2 posea
		(division entera, truncando) en cualquiera de sus paises.
		3) Si el jugador poseyera continentes completos agregara el
		adicional que indica ejercitos_por_continente obligatoriamente
		en dicho continente."""
		raise NotImplementedError

	def jugador_es_ganador(self, jugador):
		"""Verifica si el jugador gano el juego.
		Un jugador gana el juego si conquista el 100% de los paises."""
		raise NotImplementedError

	def jugador_esta_vivo(self, jugador):
		"""Verifica si un jugador sigue en carrera.
		Un jugador muere cuando se queda sin paises."""
		raise NotImplementedError

	def jugar(self):
		Interfaz.setear_titulo('Trabajo de Entrega Grupal')
		Interfaz.alertar('Bienvenido!', 'Bienvenido al Trabajo de Entrega Grupal')

		# Se selecciona el numero de jugadores y se crean los mismos:
		self.configurar_el_juego()

		# Se reparten los paises iniciales:
		self.repartir_paises()
		self.tablero.actualizar_interfaz()

		# Se sortea que jugador iniciara el juego:
		inicia_ronda = random.randrange(len(self.jugadores))

		Interfaz.setear_texto("Ronda: %s" % self.texto_ronda(inicia_ronda))

		# Primer refuerzo de ejercitos:
		self.agregar_ejercitos_inicial(inicia_ronda)

		# Bucle principal del juego:
		while Interfaz.esta_corriendo():
			# Para cada jugador en la ronda:
			for i in range(len(self.jugadores)):
				jugador = self.jugadores[(inicia_ronda + i) % len(self.jugadores)]

				# El jugador puede haber muerto durante esta ronda:
				if not self.jugador_esta_vivo(jugador):
					continue

				# El jugador juega su fase de ataques:
				paises_ganados = self.realizar_fase_ataque(jugador)

				# Se verifica si gano el juego:
				if self.jugador_es_ganador(jugador):
					Interfaz.alertar('Hay ganador!', 'El jugador %s ha ganado el juego' % jugador)
					return

				# El jugador realiza sus reagrupamientos:
				self.realizar_fase_reagrupamiento(jugador)

				# Se entrega la tarjeta y se verifica si ocupa
				# algun pais del cual posee tarjeta.
				self.manejar_tarjetas(jugador, paises_ganados)

			# Si algun jugador hubiera perdido durante la ronda
			# anterior se lo saca del juego:
			for i in range(len(self.jugadores) - 1, -1, -1):
				if not self.jugador_esta_vivo(self.jugadores[i]):
					Interfaz.alertar('Uno menos!', 'El jugador %s ha quedado eliminado' % jugador)
					self.jugadores.pop(i)
					if inicia_ronda >= i:
						inicia_ronda -= 1

			# La siguiente ronda es iniciada por el siguiente jugador:
			inicia_ronda = (inicia_ronda + 1) % len(self.jugadores)

			Interfaz.setear_texto("Ronda: %s" % self.texto_ronda(inicia_ronda))

			# Los jugadores refuerzan sus ejercitos:
			self.agregar_ejercitos(inicia_ronda)

	def texto_ronda(self, inicia_ronda):
		"""Magia negra de Python.
		(Devuelve el nombre de los jugadores en el orden de la ronda.)"""
		return ', '.join([str(x) for x in self.jugadores[inicia_ronda:] + self.jugadores[:inicia_ronda]])

if __name__ == '__main__':
	t = TEG()
	t.jugar()
