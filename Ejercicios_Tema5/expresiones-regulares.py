import re  # libreria de expresiones regulares

path = 'javascript.js'

try:
    archivo = open(path, 'r')
except:
    print('El archivo que intentas abrir no existe')
    quit()

texto = ''

for linea in archivo:
    texto += linea

# PRIMER PUNTO
patron = re.compile('(\w+( |)=( |)[\d+\.\d+|\w]+);')  # setencia de asignacion
result = patron.findall(texto)
for date in result:
    print("\x1b[1;33m"+"Sentencias de asignación: " + "\x1b[1;37m" + date[0])

# SEGUNDO PUNTO
patron2 = re.compile(
    '(\w+( |)=( |)[\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\d+\.\d+|\w]+);')  # Operaciones Aritmeticas basicas
result = patron2.findall(texto)
for date in result:
    print("\x1b[1;35m"+"Operaciones Aritmeticas basicas: " +
          "\x1b[1;37m" + date[0])

# TERCER PUNTO
patron3 = re.compile(
    '([\d+\.\d+|\w]+[ |](\={2,3}|\>|\<|\!|\>=|\<=|\!=)[ |][\d+\.\d+|\w]+)')  # Operaciones Aritmeticas basicas
result = patron3.findall(texto)
for date in result:
    print("\x1b[1;34m"+"Expresiones Booleanas: \t" + "\x1b[1;37m" + date[0])

# CUARTO PUNTO
patron4 = re.compile(
    '(\w+( |)=( |)[\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\(\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\d+\.\d+|\w]+\));')  # Operaciones Aritmeticas basicas
result = patron4.findall(texto)
for date in result:
    print("\x1b[1;31m"+"Operacines Avanzadas: \t" + "\x1b[1;37m" + date[0])

# QUINTO PUNTO
patron5 = re.compile(
    '([if|for|while|switch|forEach].*[\(]\w.*[\)]){')  # Operaciones Aritmeticas basicas
result = patron5.findall(texto)
for date in result:
    print("\x1b[1;36m"+"Estructuras de Control: \t" + "\x1b[1;37m" + date)
