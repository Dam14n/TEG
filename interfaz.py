
from Tkinter import *
import tkMessageBox
import thread
import time

from constantes import *

class Interfaz(object):
	"""Implementacion de la interfaz de usuario del TEG."""

	# Botones del mouse
	BOTON_IZQUIERDO = 0
	BOTON_DERECHO = 1

	@staticmethod
	def iniciar(paises, tablero, fondo):
		"""Inicia la interfaz grafica. Recibe un diccionario con las
		coordenadas de cada pais, el nombre de la imagen de fondo del
		tablero y el color de fondo de la ventana."""
		_Interfaz(paises, tablero, fondo)
		thread.start_new_thread(_Interfaz.instancia.crear, ())
		while not Interfaz.esta_corriendo():
			time.sleep(0.001)

	@staticmethod
	def esta_corriendo():
		"""Informa si la ventana aun esta corriendo."""
		return _Interfaz.instancia.corriendo

	@staticmethod
	def setear_titulo(titulo):
		"""Establece el titulo del tablero."""
                return Interfaz._ejecutar(_Interfaz.instancia.setear_titulo, titulo)

	@staticmethod
	def setear_texto(texto):
		"""Establece el texto del tablero."""
                return Interfaz._ejecutar(_Interfaz.instancia.setear_texto, texto)

	@staticmethod
	def ubicar_ejercitos(ejercitos):
		"""Recibe un diccionario de pares (color, ejercitos) por pais
		y los muestra en el tablero."""
		return Interfaz._ejecutar(_Interfaz.instancia.ubicar_ejercitos, ejercitos)

	@staticmethod
	def alertar(titulo, texto):
		"""Abre una ventanita de informacion con el titulo y el texto
		seleccionados."""
		return Interfaz._ejecutar(tkMessageBox.showinfo, titulo, texto)

	@staticmethod
	def preguntar(titulo, texto):
		"""Abre una ventanita de dialogo con el titulo y el texto
		seleccionados. Devuelve True o False segun la respuesta sea
		afirmativa o negativa."""
		return Interfaz._ejecutar(tkMessageBox.askyesno, titulo, texto)

	@staticmethod
	def seleccionar_pais():
		"""Aguarda a que el usuario clickee sobre algun pais. Devuelve
		una tupla (pais, boton), donde boton es
		Interfaz.BOTON_IZQUIERDO o Interfaz.BOTON_DERECHO."""
		_Interfaz.instancia.seleccion_pais = None
		while Interfaz.esta_corriendo() and not _Interfaz.instancia.seleccion_pais:
			time.sleep(0.001)
		return _Interfaz.instancia.seleccion_pais

	@staticmethod
	def elegir(titulo, texto, opciones=None):
		"""Presenta al usuario una ventanita con el titulo y el texto
		indicados para el ingreso de datos. opciones es una lista de
		las opciones a presentarle al usuario, la funcion devuelve
		el objeto de la lista seleccionado. En caso de no especificarse
		la lista de opciones la ventana contendra un cuadro de texto y
		devolvera la cadena ingresada por el usuario."""
		return Interfaz._ejecutar(_Interfaz.instancia.popup, titulo, texto, opciones)

	@staticmethod
	def _ejecutar(accion, *parametros):
		if Interfaz.esta_corriendo():
			_Interfaz.instancia.parametros = parametros
			_Interfaz.instancia.accion = accion
			while Interfaz.esta_corriendo() and _Interfaz.instancia.accion:
				time.sleep(0.01)
			return _Interfaz.instancia.retorno


# De aca en adelante son detalles de implementacion que no deberian interesarle
# a quien use la clase.


_colores = {
	COLOR_NEGRO: 'black',
	COLOR_AZUL: 'blue',
	COLOR_ROSA: 'hot pink',
	COLOR_AMARILLO: 'gold3',
	COLOR_VERDE: 'dark green',
	COLOR_ROJO: 'red',
}

def _dibujar_circulo(canvas, x, y, r, color):
	id = canvas.create_oval(x - r, y - r, x + r, y + r, fill=_colores[color])
	return id

class _Interfaz(object):
	instancia = None
	def __init__(self, paises, tablero, fondo):
		if(_Interfaz.instancia):
			raise Exception('Iniciando dos veces la interfaz')

		self.corriendo = False
		_Interfaz.instancia = self

		self.paises = paises
		self.tablero = tablero
		self.fondo = fondo

		self.accion = None
		self.parametros = None
		self.retorno = None
		self.seleccion_pais = None

	def timer(self):
		if self.accion:
			try:
				self.retorno = self.accion(*self.parametros)
			except Exception, e:
				print e
			finally:
				self.accion = None
		else:
			self.actualizar_pais()
			time.sleep(0.001)
		self.ventana.after(1, self.timer)

	def actualizar_pais(self):
		x, y = self.ventana.winfo_pointerxy()
		x -= self.canvas.winfo_rootx()
		y -= self.canvas.winfo_rooty()

		if 0 <= x <= self.canvas.winfo_width() and 0 <= y <= self.canvas.winfo_height():
			if self.ultimo_x != x or self.ultimo_y != y:
				self.ultimo_x = x
				self.ultimo_y = y
				#self.pie['text'] = "%d, %d: %s" % (x, y, self._encontrar_pais(x, y))
				p = self.encontrar_pais(x, y)
				self.pie['text'] = 'Pais: %s' % p if p else ''

	def encontrar_pais(self, x, y, r=25):
		mp = None
		md = 10000
		for p in self.paises:
			x0, y0 = self.paises[p]
			d = ((x0 - x) ** 2 + (y0 - y) ** 2) ** .5
			if d < md:
				md = d
				mp = p
		if mp and md <= r:
			return mp
		return None

	def click(self, event):
		#print event.x, event.y
		pais = self.encontrar_pais(event.x, event.y)
		if pais:
			self.seleccion_pais = (pais, Interfaz.BOTON_IZQUIERDO if event.num == 1 else Interfaz.BOTON_DERECHO)

	def crear(self):
		self.ultimo_x = -1
		self.ultimo_y = -1

		self.ventana = Tk()
		self.ventana.title('Trabajo de Entrega Grupal')
		self.ventana['bg'] = self.fondo
		self.ventana.resizable(width=FALSE, height=FALSE)

		self.titulo = Label(self.ventana, bg=self.fondo, font=('Times', 14))
		self.titulo.pack(side=TOP)

		self.texto = Label(self.ventana, bg=self.fondo)
		self.texto.pack(side=TOP)

		self.img = PhotoImage(file=self.tablero)

		self.canvas = Canvas(self.ventana, width=self.img.width(), height=self.img.height())
		self.canvas.create_image(0,0, anchor=NW, image=self.img)
		self.canvas['highlightthickness'] = 0
		self.canvas.pack()

		self.canvas.bind('<Button-1>', self.click)
		self.canvas.bind('<Button-3>', self.click)

		self.pie = Label(self.ventana)
		self.pie['bg'] = self.fondo
		self.pie.pack(side=BOTTOM)

		self.corriendo = True
		self.ventana.after(1, self.timer)
		self.ventana.mainloop()
		self.corriendo = False

	def popup(self, titulo, texto, opciones=None):
		top = Toplevel(self.ventana)
		top.transient(self.ventana)
		top.geometry('+%d+%d' % (self.ventana.winfo_rootx()+self.ventana.winfo_width()/2-100, self.ventana.winfo_rooty()+self.ventana.winfo_height()/2-50))
		top.focus_set()
		top.title(titulo)

		msg = Message(top, text=texto, width=200)
		msg.pack()

		var = StringVar(top)
		if opciones:
			var.set(str(opciones[0]))
			opt = OptionMenu(top, var, *[str(x) for x in opciones])
		else:
			opt = Entry(top, textvariable=var)
		opt.pack()

		button = Button(top, text='OK', command=top.destroy)
		button.pack()

		self.ventana.wait_window(top)

		if opciones:
			for o in opciones:
				if str(o) == var.get():
					return o
			return None
		return var.get()

	def ubicar_ejercitos(self, ejercitos):
		for pais in ejercitos:
			x, y = self.paises[pais]
			_dibujar_circulo(self.canvas, x, y, 7, ejercitos[pais][0])
			canvas_id = self.canvas.create_text(x, y, font=('Sans', -9, 'bold'), fill='white')
	        	#canvas.itemconfig(canvas_id, text=p)
		        self.canvas.itemconfig(canvas_id, text='%d' % ejercitos[pais][1])

	def setear_titulo(self, titulo):
		_Interfaz.instancia.titulo['text'] = titulo

	def setear_texto(self, texto):
		_Interfaz.instancia.texto['text'] = texto

