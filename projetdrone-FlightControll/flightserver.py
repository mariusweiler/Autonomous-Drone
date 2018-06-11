import socket

class socketFlightServer():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('172.20.10.6', 9050))
    server_socket.listen(1)  # allow only 1 connection
    connection, client_address = server_socket.accept()

    def waitHeightOk(self):
        heightOk=0;
  	while not heightOk:
   	    data = connection.recv(1024)
   	    if data:
                if not isinstance(data, list) and data > 130:
                    heightOk=1;

    def getPersonPosition(self):
   	positionReceived=0;
   	data=0;
  	while not positionReceived:
   	    data = connection.recv(1024)
   	    if data:
                if type(data) != 'int':
                    positionReceived=1;
   	return data

    def closeSocket():
        server_socket.close()
   	connection.close()

