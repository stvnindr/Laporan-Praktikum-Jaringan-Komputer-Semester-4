from socket import *

serverName = 'localhost'
serverPort = 12000

# GUNAKAN SOCK_DGRAM untuk UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# UDP tidak perlu clientSocket.connect() secara formal, 
# tapi bisa dilakukan untuk menetapkan alamat default. 
# Namun umumnya langsung dikirim:

sentence = input('Input lowercase sentence: ')

# Kirim pesan (dengan tujuan alamat server)
clientSocket.sendto(sentence.encode(), (serverName, serverPort))

# Cukup terima datanya saja, tidak perlu serverAddress
modifiedMessage = clientSocket.recv(2048)

print('From Server:', modifiedMessage.decode())

clientSocket.close()