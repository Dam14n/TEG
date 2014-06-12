from interfaz import Interfaz
from constantes import *

class Jugador(object):
	"""Representa a un jugador de TEG."""
	def __init__(self, color, nombre):
		"""Crea un jugador desde un color y un nombre."""
		self.color = color
		self.nombre = nombre
		self.tarjetas = {}
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
		restricciones = {}
		pais_origen = True
		while pais_origen:
			pais_origen = self.pedir_pais_propio(tablero, "%s esta reagrupando. Seleccionar pais de origen." % self)
			while pais_origen and not tablero.ejercitos_pais(pais_origen) > 1:
				pais_origen = self.pedir_pais_propio(tablero, "%s esta reagrupando. Seleccionar pais de origen." % self)

			if pais_origen:

				ejercitos_posibles = tablero.ejercitos_pais(pais_origen)
				if restricciones.has_key(pais_origen): # Si esta en restricciones es porque se hizo un reagrupamiento previo, al pais elegido.
					ejercitos_posibles -= restricciones[pais_origen]
				if ejercitos_posibles == 1: continue # Si es 1 ya no puede mover mas ejercitos desde ese pais.

				cantidad_a_mover = Interfaz.elegir(self, 'Cuantos ejercitos se desplazan de %s?' % pais_origen, range(1, ejercitos_posibles))

				pais_destino = self.pedir_pais_propio(tablero, '%s esta reagrupando. Seleccionar pais de destino.' % self)
				while pais_destino and not tablero.es_limitrofe(pais_origen, pais_destino):
					pais_destino = self.pedir_pais_propio(tablero, '%s esta reagrupando. Seleccionar pais de destino.' % self)
				if not pais_destino: continue

				cantidad_a_poner = cantidad_a_mover
				cantidad_a_sacar = cantidad_a_mover
				if restricciones.has_key(pais_origen):
					cantidad_a_sacar += restricciones[pais_origen]
				if restricciones.has_key(pais_destino):
					cantidad_a_poner += restricciones[pais_destino]


				restricciones[pais_origen] = restricciones.get(pais_origen, 0) + cantidad_a_mover
				reagrupamientos.append((pais_origen, pais_destino, cantidad_a_mover))
				tablero.actualizar_interfaz({pais_origen: - cantidad_a_sacar, pais_destino: cantidad_a_poner})
		return reagrupamientos

	def pedir_pais_propio(self, tablero, mensaje):
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
		"""Devuelve el color del jugador"""
		return self.color

	def su_nombre(self):
		"""Devuelve el nombre del jugador"""
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
                if tarjeta.su_tipo() in self.tarjetas.keys():
                    paises = self.tarjetas[tarjeta.su_tipo()]
                    paises.append(tarjeta)
                    self.tarjetas[tarjeta.su_tipo()] = paises
                else:
                    self.tarjetas[tarjeta.su_tipo()] = [tarjeta]

	def devolver_tarjeta(self, mazo, tipo_tarjeta):
		"""Devuelve la tarjeta canjeada al mazo"""
		for tipo_t in self.tarjetas:
                    if tipo_tarjeta == tipo_t:
                        if len(self.tarjetas[tipo_t]) == 1:
                            mazo.devolver_tarjeta(self.tarjetas.pop(tipo_t))
                        else:
                            mazo.devolver_tarjeta(self.tarjetas[tipo_t].pop(0))
                        return
