import os

def getScriptDirectory(): # ritorna il percorso dove si trova lo script senza separatore finale
	return os.path.dirname(os.path.realpath(__file__))
    