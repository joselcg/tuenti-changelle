# Importamos las librerias necesarias
import socket
# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 2003 # Puerto de comunicacion
# Realizamos la conexion al la IP y puerto
sock.connect(('52.49.91.111',port))
# Leemos los datos del servidor
data = sock.recv(4096)
print(data.decode())
#sock.send('1U2L')
#data = sock.recv(1000)
#print(data.decode())










sock.close()