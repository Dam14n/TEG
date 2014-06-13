Diseño:
El programa TEG consiste en un juego de estrategia el cual se basa en un mapamundi y a cada jugador se le asigna la misma cantidad de países hasta completar el mapa.
En primer lugar hay que desarrollar la clase teg la cual se encarga de la lógica principal del juego:
Se inicia el juego, se configuran los jugadores, se reparten los países para cada jugador(1 por cada país de forma inicial), se elige el jugador inicial y se empieza la ronda de agregar ejércitos:

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
Luego se comienza con ciclo infinito el cual finaliza cuando un jugador gana, el cual consiste de lo siguiente:
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
                                        Interfaz.alertar('Uno menos!', 'El jugador %s ha quedado eliminado' % self.jugadores[i])
					self.jugadores.pop(i)
					if inicia_ronda >= i:
						inicia_ronda -= 1

			# La siguiente ronda es iniciada por el siguiente jugador:
			inicia_ronda = (inicia_ronda + 1) % len(self.jugadores)
                        
			Interfaz.setear_texto("Ronda: %s" % self.texto_ronda(inicia_ronda))

			# Los jugadores refuerzan sus ejércitos:
			self.agregar_ejercitos(inicia_ronda)

En primer lugar se comprueba que durante la ronda el jugador no esté muerto, en caso contrario el juego continua. Se realiza la fase de ataques del jugador el cual consta de lo siguiente:
def realizar_fase_ataque(self, jugador):
		Este método implementa la fase de ataque de un jugador. Sucesivamente hace combatir a los países seleccionados. Si el país atacante conquista al país atacado, avisa al jugador que gano el país y cuantos ejércitos desea mover hasta un máximo de 3 ejércitos. Devuelve el número de países conquistados por el jugador.
Utiliza la clase dados para realizar la tirada de los dados y comprobar que dados ganaron y cuales perdieron, con una  condición la cual es que cada jugador no puede tirar con más de 3 dados y los dados se comparan de la siguiente forma: 
Se ordenan los dados de mayor a menor tanto del atacante como del atacado y se comparan. Si los dados del atacado son iguales o mayores gana el dado atacado, en caso contrario que el dado sea menor que el dado atacante pierde.
Luego de finalizar los ataques el jugador puede reagrupar sus ejércitos con un mínimo de 1 ejercito por país y puede mover la cantidad de ejércitos que desee, con la condición de que ambos países sean limítrofes. Esto se realiza con el método, el cual recibe al jugador actual:
def realizar_fase_reagrupamiento(self, jugador):
Posterior al reagrupamiento de ejércitos, si el jugador realizo menos de 3 canjes y gano al menos un país o si realizo 3 o mas canjes y gano al menos dos países, recibe una nueva tarjeta de país. Además si el jugador posee una tarjeta de un país que posee automáticamente se le agregan al país 2 ejércitos. Esto se realiza con el método, el cual recibe el jugador actual y la cantidad de países que gano, este método muestra por pantalla el canje por país:
		def manejar_tarjetas(self, jugador, paises_ganados):
Terminada la fase de obtención de tarjeta si alguno de los jugadores perdió se lo quita de la lista de jugadores y se continua con el juego, en este paso se cambia el jugador que inicia la partida, ejemplo en un juego de 2 jugadores, si en la primer ronda inicio el jugador 1 en la segunda ronda va a iniciar el jugador 2 y así sucesivamente. Luego de cambiar de jugador se procede a agregar los ejércitos, con el siguiente método: 
def agregar_ejercitos(self, inicia_ronda):
Este método recibe el jugador que inicia la ronda y se encarga de calcular cuántos ejércitos tiene que agregar en el mapa. Para esto tiene que cumplir con las siguientes condiciones:
El jugador va a recibir una cantidad de ejércitos igual a la mitad de los países que posee para poder agregar por todo el mapa. También si posee 3 tarjetas diferentes o 3 iguales puede realizar un canje y recibe ejércitos para poner por todo el mapa, en el siguiente orden:
Primer canje: 4 ejércitos, Segundo canje : 7 ejércitos y 3 o más canjes:  la cantidad de canjes por 5(serian 2 canjes realizados, sin contar el actual, por 5 = 10 , en el tercer canje)
Se calculan entonces los ejércitos según la cantidad de países y según los canjes.  Además se calcula la cantidad de ejércitos por el continente ya que si se posee un continente completo tiene a disposición ejércitos solo para el continente conquistado.
Este método utiliza los siguientes métodos:
 def calcular_ejercitos(self,jugador):
Se calcula la cantidad de ejércitos por canje, el cual recibe el jugador actual
def comprobar_continentes(self,jugador):
Se calcula la cantidad de ejércitos según si posee el continente completo, el jugador actual.
def comprobar_canje(self,jugador):
Se calcula la cantidad de ejércitos según el canje realizado por 3 tarjetas iguales o 3 diferentes. Además se encarga de devolver las tarjetas usadas al mazo y de mostrar por pantalla que tarjetas se canjearon. 
Este ciclo se repite hasta que solo quede un jugador en el mapa que conquiste todo el mundo.
La clase teg tiene los siguientes atributos:
self.mazo = Mazo(paises.paises_por_tarjeta)
Este atributo hace referencia al mazo del juego el cual posee las tarjetas de los países. Esta clase posee el mazo con las cartas del juego que se van retirando y otro mazo con las cartas usadas en caso de que el mazo quede vacío se mezclan las cartas usadas y se vuelve a formar el mazo. El mazo está formado por tarjetas que poseen un tipo(globo, galeón, comodín o canon) y un país. El mazo cuenta con los métodos para sacar una tarjeta del mazo, calcular la cantidad de tarjetas disponibles, devolver a un nuevo mazo las tarjetas usadas, se puede mezclar el mazo y llenarlo.
		self.dados = Dados()
Los dados representan la lógica de tirar los dados, 1 dado por cada ejército. En donde recibe la cantidad de ejército del atacante y del atacado. Verifica que si tienen más de 3 ejércitos se tiren un máximo de 3 dados.  Comprueba que dados ganaron y perdieron y los guarda en una variable llamada ejercitos_atacantes_perdidos y ejercitos_atacados_perdidos. Posteriormente el método de la fase de ataque de la clase teg se le piden estos atributos para modificar el tablero del mapa.
		self.tablero = Tablero(paises.paises_por_continente, paises.paises_limitrofes)
Representa la lógica de un tablero el cual posee países con los siguientes atributos:
Nombre del país, color del jugador que posee el país, cantidad de ejército, a que continente pertenece y sus países limítrofes. Una vez que se abre el tablero, se encarga de calcular los países y los continentes. Cada  vez que se conquista un país en la fase de ataque, se debe modificar el tablero, al igual que cuando se reagrupan los ejércitos se debe actualizar el tablero.
Esta clase cuenta con los métodos para ocupar el país, asignar los ejércitos a un país, actualizar el tablero, devolver los siguientes datos: el color de un país, la cantidad de ejércitos de un país, si es limítrofe, la cantidad d de países del mapa, la cantidad de países del continente, si el país está en un continente y una lista con todos los países que posee un jugador.
		self.tarjetas_usadas = {}
Representa las tarjetas usadas por los jugadores a la hora de canjear las tarjetas por el país, si posee dicho país recibe 2 ejércitos en el país y se guarda el jugador y el país del cual realizo el canje.
		self.jugadores = []
Representa una lista de los jugadores que están jugando. Utiliza la clase Jugador por cada jugador.
La clase jugador implementa la lógica de un jugador, el cual posee un nombre, un color , tarjetas y la cantidad  de canjes que realizo.
Cada jugador puede atacar a otro jugador, agregar ejércitos a sus países, reagrupar los ejércitos de sus países. También se le puede pedir al jugador su color, su nombre, que tarjetas posee, cuantos canjes realizo, puede retirar una tarjeta del mazo y guardarla en sus tarjetas y devolver tarjetas al mazo  a  la hora de realizar un canje.
Interfaz.iniciar(paises.coordenadas_de_paises, paises.archivo_tablero, paises.color_tablero)
La interfaz es la encargada de la interacción entre el jugador y el tablero, la misma recibe mensajes del tablero y le indica al jugador lo que debe hacer, Ej: jugador negro, en etapa de reagrupamiento. Le dice al jugador que debe reagrupar sus ejércitos.
También se utilizan constantes que representan los países por continentes, la cantidad de ejércitos que se pueden canjear por continente, los países limítrofes, que tipo de tarjeta corresponde a cada país, los tipos de tarjetas que hay en el juego (comodín, galeón, globo, cañón) y los colores que pueden tener los ejércitos de los jugadores que son : negro, rojo , azul, rosa , amarillo y verde.
