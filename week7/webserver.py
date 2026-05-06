# import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 7621
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1)             
# Fill in end

while True:
    # Establish the connection
    print('Server Siap...')

    connectionSocket, addr = serverSocket.accept() 
    # Fill in end
    
    try:
        # Fill in start
        message = connectionSocket.recv(1024).decode() 
        # Fill in end
        
        filename = message.split()[1]
        f = open(filename[1:])
        
        outputdata = f.read() 
        # Fill in end
      
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        # Fill in end
        
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
        
    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        connectionSocket.close()
        
serverSocket.close()
sys.exit() 