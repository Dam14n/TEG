# Este archivo define la configuracion de paises del TEG clasico.

from constantes import *

# Continentes con todos sus paises:
paises_por_continente = {
	'Africa': ['Egipto', 'Etiopia', 'Madagascar', 'Sahara', 'Sudafrica', 'Zaire'],
	'America del Sur': ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Peru', 'Uruguay'],
	'America del Norte': ['Alaska', 'California', 'Canada', 'Groenlandia', 'Labrador', 'Nueva York', 'Mexico', 'Oregon', 'Terranova', 'Yukon'],
	'Asia': ['Arabia', 'Aral', 'China', 'Gobi', 'India', 'Iran', 'Israel', 'Japon', 'Kamchatka', 'Malasia', 'Mongolia', 'Siberia', 'Taimir', 'Tartaria', 'Turquia'],
	'Europa': ['Alemania', 'Espana', 'Francia', 'Gran Bretana', 'Islandia', 'Italia', 'Polonia', 'Rusia', 'Suecia'],
	'Oceania': ['Australia', 'Borneo', 'Java', 'Sumatra'],
}

# Cantidad de ejercitos que pone un jugador si conquista el continente
ejercitos_por_continente = {
	'Africa': 3,
	'America del Sur': 3,
	'America del Norte': 5,
	'Asia': 7,
	'Europa': 5,
	'Oceania': 2,
}

# Cada pais con sus paises linderos:
paises_limitrofes = {
	'Alaska': ['Kamchatka', 'Oregon', 'Yukon'],
	'Alemania': ['Francia', 'Gran Bretana', 'Italia', 'Polonia'],
	'Arabia': ['Israel', 'Turquia'],
	'Aral': ['Iran', 'Mongolia', 'Rusia', 'Siberia', 'Tartaria'],
	'Argentina': ['Brasil', 'Chile', 'Peru', 'Uruguay'],
	'Australia': ['Borneo', 'Chile', 'Java', 'Sumatra'],
	'Borneo': ['Australia', 'Malasia'],
	'Brasil': ['Argentina', 'Colombia', 'Peru', 'Sahara', 'Uruguay'],
	'California': ['Mexico', 'Nueva York', 'Oregon'],
	'Canada': ['Nueva York', 'Oregon', 'Terranova', 'Yukon'],
	'Chile': ['Argentina', 'Australia', 'Peru'],
	'China': ['Gobi', 'India', 'Iran', 'Japon', 'Kamchatka', 'Malasia', 'Mongolia', 'Siberia'],
	'Colombia': ['Brasil', 'Mexico', 'Peru'],
	'Egipto': ['Etiopia', 'Israel', 'Madagascar', 'Sahara', 'Polonia', 'Turquia'],
	'Espana': ['Francia', 'Gran Bretana', 'Sahara'],
	'Etiopia': ['Egipto', 'Sahara', 'Sudafrica', 'Zaire'],
	'Francia': ['Alemania', 'Espana', 'Italia'],
	'Gobi': ['China', 'Iran', 'Mongolia'],
	'Gran Bretana': ['Alemania', 'Espana', 'Islandia'],
	'Groenlandia': ['Islandia', 'Labrador', 'Nueva York'],
	'India': ['China', 'Iran', 'Malasia', 'Sumatra'],
	'Iran': ['Aral', 'China', 'Gobi', 'India', 'Mongolia', 'Rusia', 'Turquia'],
	'Islandia': ['Gran Bretana', 'Groenlandia', 'Suecia'],
	'Israel': ['Arabia', 'Egipto', 'Turquia'],
	'Italia': ['Alemania', 'Francia'],
	'Japon': ['China', 'Kamchatka'],
	'Java': ['Australia'],
	'Kamchatka': ['Alaska', 'China', 'Japon', 'Siberia'],
	'Labrador': ['Groenlandia', 'Terranova'],
	'Madagascar': ['Egipto', 'Zaire'],
	'Malasia': ['Borneo', 'China', 'India'],
	'Mexico': ['California', 'Colombia'],
	'Mongolia': ['Aral', 'China', 'Gobi', 'Iran', 'Siberia'],
	'Nueva York': ['California', 'Canada', 'Groenlandia', 'Oregon', 'Terranova'],
	'Oregon': ['Alaska', 'California', 'Canada', 'Nueva York', 'Yukon'],
	'Peru': ['Argentina', 'Brasil', 'Chile', 'Colombia'],
	'Polonia': ['Alemania', 'Egipto', 'Turquia', 'Rusia'],
	'Rusia': ['Aral', 'Iran', 'Polonia', 'Suecia', 'Turquia'],
	'Sahara': ['Brasil', 'Egipto', 'Espana', 'Etiopia', 'Zaire'],
	'Siberia': ['Aral', 'China', 'Kamchatka', 'Mongolia', 'Taimir', 'Tartaria'],
	'Sudafrica': ['Etiopia', 'Zaire'],
	'Suecia': ['Islandia', 'Rusia'],
	'Sumatra': ['Australia', 'India'],
	'Taimir': ['Siberia', 'Tartaria'],
	'Tartaria': ['Aral', 'Siberia', 'Taimir'],
	'Terranova': ['Canada', 'Labrador', 'Nueva York'],
	'Turquia': ['Arabia', 'Egipto', 'Iran', 'Israel', 'Polonia', 'Rusia'],
	'Uruguay': ['Argentina', 'Brasil'],
	'Yukon': ['Alaska', 'Canada', 'Oregon'],
	'Zaire': ['Etiopia', 'Madagascar', 'Sahara', 'Sudafrica'],
}

# Que tipo de tarjeta corresponde para cada pais:
paises_por_tarjeta = {
	TARJETA_COMODIN: ['Argentina', 'Taimir'],
	TARJETA_GALEON: ['Alaska', 'Alemania', 'Borneo', 'Brasil', 'China', 'Gran Bretana', 'Groenlandia', 'Islandia', 'Israel', 'Madagascar', 'Mongolia', 'Nueva York', 'Peru', 'Siberia', 'Suecia', 'Turquia', 'Zaire'],
	TARJETA_GLOBO: ['Chile', 'Colombia', 'Egipto', 'Espana', 'Etiopia', 'Francia', 'Gobi', 'India', 'Iran', 'Italia', 'Kamchatka', 'Rusia', 'Sumatra', 'Uruguay', 'Yukon'],
	TARJETA_CANON: ['Arabia', 'Aral', 'Australia', 'California', 'Canada', 'Japon', 'Java', 'Labrador', 'Malasia', 'Mexico', 'Oregon', 'Polonia', 'Sahara', 'Sudafrica', 'Tartaria', 'Terranova'],
}

# Tablero de juego:
archivo_tablero = 'tablero.gif'
color_tablero = '#ffdd55'

# Coordenadas del centro de cada pais en unidades del tablero (origen arriba a la izquierda):
coordenadas_de_paises = {
	'Chile': (264, 324),
	'Argentina': (294, 320),
	'Uruguay': (324, 308),
	'Peru': (271, 272),
	'Brasil': (331, 265),
	'Colombia': (276, 239),
	'Alaska': (50, 145),
	'Yukon': (101, 113),
	'Canada': (150, 84),
	'Groenlandia': (291, 71),
	'Oregon': (100, 169),
	'Nueva York': (162, 128),
	'Terranova': (190, 121),
	'Labrador': (231, 104),
	'California': (136, 186),
	'Mexico': (195, 198),
	'Islandia': (366, 150),
	'Suecia': (484, 99),
	'Gran Bretana': (446, 161),
	'Espana': (429, 238),
	'Francia': (479, 191),
	'Italia': (520, 240),
	'Alemania': (516, 174),
	'Polonia': (552, 176),
	'Rusia': (554, 128),
	'Sahara': (496, 294),
	'Zaire': (539, 332),
	'Etiopia': (568, 311),
	'Egipto': (588, 287),
	'Sudafrica': (573, 361),
	'Madagascar': (624, 329),
	'Sumatra': (663, 270),
	'Borneo': (714, 254),
	'Java': (741, 255),
	'Australia': (721, 316),
	'Aral': (575, 84),
	'Tartaria': (598, 75),
	'Taimir': (621, 75),
	'Siberia': (642, 94),
	'Kamchatka': (674, 75),
	'Iran': (616, 157),
	'Mongolia': (631, 124),
	'Gobi': (660, 151),
	'China': (689, 127),
	'Japon': (730, 88),
	'Turquia': (616, 193),
	'Israel': (602, 223),
	'Arabia': (629, 233),
	'India': (686, 221),
	'Malasia': (734, 202)
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
