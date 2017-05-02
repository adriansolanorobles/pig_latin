pyg = 'ei'

original = raw_input('Escribe una palabra:')

if len(original) > 0 and original.isalpha():
    palabra = original.lower()
    primera = palabra[0].lower()
    
    if primera == "a" or primera == "e" or primera == "i" or primera == "o" or primera == "u":
        nueva_palabra = palabra + pyg
    else:
        nueva_palabra = palabra[1:] + palabra[0:1] + pyg
else:
	print 'Vacío'
