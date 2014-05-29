
# Este archivo define la configuracion de paises de la Argentina

from constantes import *

paises_por_continente = {
	'Centro': ['Buenos Aires', 'Cordoba', 'La Pampa'],
	'Cuyo': ['La Rioja', 'Mendoza', 'San Juan', 'San Luis'],
	'Litoral': ['Chaco', 'Corrientes', 'Entre Rios', 'Formosa', 'Misiones', 'Santa Fe'],
	'Noroeste': ['Catamarca', 'Jujuy', 'Salta', 'Santiago del Estero', 'Tucuman'],
	'Patagonia': ['Chubut', 'Neuquen', 'Rio Negro', 'Santa Cruz'],
}

ejercitos_por_continente = {
	'Centro': 2,
	'Cuyo': 2,
	'Litoral': 3,
	'Noroeste': 3,
	'Patagonia': 2,
}

paises_limitrofes = {
	'Buenos Aires': ['Entre Rios', 'Santa Fe', 'Cordoba', 'La Pampa', 'Rio Negro'],
	'Catamarca': ['Salta', 'Tucuman', 'La Rioja', 'Santiago del Estero'], # Falta Cdba.
	'Chaco': ['Formosa', 'Corrientes', 'Santa Fe', 'Santiago del Estero', 'Salta'],
	'Chubut': ['Rio Negro', 'Santa Cruz'],
	'Cordoba': ['Santiago del Estero', 'Santa Fe', 'Buenos Aires', 'La Pampa', 'San Luis', 'La Rioja'],
	'Corrientes': ['Misiones', 'Chaco', 'Santa Fe', 'Entre Rios'],
	'Entre Rios': ['Corrientes', 'Santa Fe', 'Buenos Aires'],
	'Formosa': ['Salta', 'Chaco'],
	'Jujuy': ['Salta'],
	'La Pampa': ['Cordoba', 'Buenos Aires', 'Rio Negro', 'Mendoza', 'San Luis'],
	'La Rioja': ['Catamarca', 'Cordoba', 'San Luis', 'San Juan'],
	'Mendoza': ['San Juan', 'San Luis', 'La Pampa', 'Neuquen'],
	'Misiones': ['Corrientes'],
	'Neuquen': ['Mendoza', 'Rio Negro'],
	'Rio Negro': ['La Pampa', 'Buenos Aires', 'Chubut', 'Neuquen'],
	'Salta': ['Jujuy', 'Formosa', 'Chaco', 'Santiago del Estero', 'Tucuman', 'Catamarca'],
	'San Juan': ['La Rioja', 'San Luis', 'Mendoza'],
	'San Luis': ['Cordoba', 'La Pampa', 'Mendoza', 'San Juan', 'La Rioja'],
	'Santa Cruz': ['Chubut'],
	'Santa Fe': ['Chaco', 'Corrientes', 'Entre Rios', 'Buenos Aires', 'Cordoba', 'Santiago del Estero'],
	'Santiago del Estero': ['Chaco', 'Santa Fe', 'Cordoba', 'Catamarca', 'Tucuman', 'Salta'],
	'Tucuman': ['Salta', 'Santiago del Estero', 'Catamarca'],
}

paises_por_tarjeta = {
	TARJETA_GALEON: ['Buenos Aires', 'La Rioja', 'Santa Fe', 'Santiago del Estero', 'Cordoba', 'Formosa', 'Jujuy'],
	TARJETA_GLOBO: ['La Pampa', 'Santa Cruz', 'Salta', 'Corrientes', 'Mendoza', 'Misiones', 'Catamarca'],
	TARJETA_CANON: ['Entre Rios', 'San Juan', 'Tucuman', 'Neuquen', 'Rio Negro', 'Chaco', 'Chubut'],
	TARJETA_COMODIN: ['San Luis'],
}

archivo_tablero = 'argentina.gif'
color_tablero = '#d0e2ff'

coordenadas_de_paises = {
	'Misiones': (80, 30),
	'Corrientes': (150, 85),
	'Entre Rios': (238, 103),
	'Formosa': (78, 140),
	'Chaco': (121, 153),
	'Santa Fe': (203, 141),
	'Salta': (108, 261),
	'Jujuy': (73, 276),
	'Santiago del Estero': (159, 217),
	'Tucuman': (147, 259),
	'Catamarca': (163, 293),
	'Cordoba': (249, 196),
	'Buenos Aires': (353, 92),
	'La Pampa': (396, 200),
	'La Rioja': (228, 276),
	'San Juan': (265, 300),
	'San Luis': (295, 239),
	'Mendoza': (337, 272),
	'Neuquen': (452, 269),
	'Rio Negro': (476, 202),
	'Chubut': (577, 221),
	'Santa Cruz': (695, 219),
}

if __name__ == '__main__':
	paises = []
	for ps in paises_por_continente.values():
		for p in ps:
			if p in paises:
				print '%s repetido' % p
			paises.append(p)

	for p in paises:
		if p not in paises_limitrofes:
			print 'faltan fronteras de %s' % p
		for f in paises_limitrofes[p]:
			if f not in paises:
				print 'frontera a pais inexistente %s => %s' % (p, f)

	for p in paises_limitrofes:
		if p not in paises:
			print 'falta continente para %s' % p

	for p in paises_limitrofes:
		for f in paises_limitrofes[p]:
			if p not in paises_limitrofes[f]:
				print 'falta frontera %s => %s' % (f, p)

	for ps in paises_por_tarjeta.values():
		for p in ps:
			if p not in paises:
				print '%s sin tarjeta' % p

	for p in coordenadas_de_paises:
		if p not in paises:
			print '%s sin coordenadas' % p

	print '%d paises' % len(paises)
	print '%d continentes' % len(paises_por_continente)
	print '%s = %d paises por tarjeta' % (', '.join(['%d' % len(x) for x in paises_por_tarjeta.values()]), sum([len(x) for x in paises_por_tarjeta.values()]))
	for c in paises_por_continente:
		print '%s: %d paises' % (c, len(paises_por_continente[c]))
