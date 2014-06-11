
from interfaz import Interfaz
from constantes import *

class Jugador(object):
	"""Representa a un jugador de TEG."""
	def __init__(self, color, nombre):
		"""Crea un jugador desde un color y un nombre."""
		self.color = color
		self.nombre = nombre
		self.tarjetas = []
		self.canjes = 0

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
		ejercitos_a_poner = sum(cantidad.values())
		asignaciones = {}
		while ejercitos_a_poner:
			pais_elegido = self.pedir_pais_propio(tablero, "%s en etapa de asignacion. Seleccionar pais." % self)
			while pais_elegido and not (cantidad[""] or cantidad.get(tablero.continente_pais(pais_elegido), 0)):
				pais_elegido = self.pedir_pais_propio(tablero, "%s en etapa de asignacion. Seleccionar pais." % self)
			if pais_elegido:
				if cantidad.has_key(tablero.continente_pais(pais_elegido)): cantidad[tablero.continente_pais(pais_elegido)] -= 1
				else: cantidad[""] -= 1
				asignaciones[pais_elegido] = asignaciones.get(pais_elegido, 0) + 1
				ejercitos_a_poner -= 1
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
		reagrupamientos = []
		pais_origen = self.pedir_pais_propio(tablero, "%s en etapa de reagrupamiento. Seleccionar pais de origen." % self)
		while pais_origen:
			while pais_origen and tablero.ejercitos_pais(pais_origen) > 1:
				pais_origen = self.pedir_pais_propio(tablero, "%s en etapa de reagrupamiento. Seleccionar pais de origen." % self)
			if pais_origen:
				# creo la lista desde 1 hasta la cantidad de ejercitos del pais menos 1, ya que si o si uno se tiene que quedar.
				cantidad_a_mover = Interfaz.elegir("Reagrupamiento", "Ejercitos del pais %s." % pais_origen, [cantidad for cantidad in xrange(1, tablero.ejercitos_pais(pais_origen) - 1)])
				pais_destino = pedir_pais_propio(tablero, '%s esta reagrupando. Seleccionar pais de destino.' % self)
				while pais_destino and not tablero.es_limitrofe(pais_origen, pais_destino):
					pais_destino = pedir_pais_propio(tablero, '%s esta reagrupando. Seleccionar pais de destino.' % self)
				if not pais_destino: continue
				reagrupamientos.append((pais_origen, pais_destino, cantidad_a_mover))
				tablero.actualizar_interfaz({pais_origen: - cantidad_a_mover, pais_destino: cantidad_a_mover})
				tablero.asignar_ejercitos(pais_origen, - cantidad_a_mover)
				tablero.asignar_ejercitos(pais_destino, cantidad_a_mover)
		return reagrupamientos

	def pedir_pais_propio(self, mensaje):
		"""Recibe una cadena de texto y lo escribe en el titulo.
		Pide al jugador que seleccione un pais que sea suyo.
		Si clickea un pais suyo con click izquierdo, devuelve el pais.
		Si hace click derecho, devuelve None."""
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
	
	def sus_tarjetas(self):
		"""Devuelve las tarjetas del jugador"""
		return self.tarjetas
	
	def canjes_realizados(self):
		"""Devuelve la cantidad de canjes del jugador"""
		return self.canjes
		
	def agregar_canje(self):
		"""Agrega un canje al jugador"""
		self.canjes += 1
		
	def asignar_tarjeta(self,tarjeta):
		"""Se le asigna una tarjeta al jugador"""
		self.tarjetas.append(tarjeta)
	
	def devolver_tarjeta(self, mazo, tipo_tarjeta):
		"""Devuelve la tarjeta canjeada al mazo"""
		for tarjeta in self.tarjetas:
                    if tipo_tarjeta == tarjeta.tipo():
                        mazo.devolver_tarjeta(self.tarjetas.pop(tarjeta))
						return
	
