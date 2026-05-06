from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)


running = True
while running:
    message = input("> ")

    if message == "exit":
        clientSocket.sendto(message.encode(), (serverName, serverPort)) 
        print("Exiting program...")
        running = False 
        continue

#mengirim pesan ke server
    clientSocket.sendto(message.encode(), (serverName, serverPort))

#menerima balasan dari server
modified_message, serverAddress = clientSocket.recvfrom(2048)
print("pesan diterima dari: ", )
print(modified_message.decode())

clientSocket.close()
print("Koneksi ditutup.")