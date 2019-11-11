from enum import Enum

class TipoDenunciaEnum(Enum):
	PODA = 'Poda'
	FALTA_CANTERO = 'Falta Cantero'
	EXTRACCION = 'Extraccion'
	ARBOL_EXISTENTE = 'Arbol Existente'
	MANTENIMIENTO = 'Mantenimiento'


	@classmethod
	def choices(cls):
		return (tuple((key.name, key.value) for key in cls))

class TipoPostEnum(Enum):
	DENUNCIA = 'DENUNCIA'
	INFORMATIVO = 'INFORMATIVO'


	@classmethod
	def choices(cls):
		return (tuple((key.name, key.value) for key in cls))