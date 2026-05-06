from socket import *

#membuat socket untuk server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

#menghubungkan (bind)
serverSocket.bind(
    ('', serverPort)
)

print("Server siap digunakan...") 

#dijalankan, selama running bernilai True
running = True
while running:
    message, clientAddress = serverSocket.recvfrom(2048)
    decodeMessage = message.decode()

    if decodeMessage.lower() == "exit":
        print("System telah diberhentikan.")
        running = False 
        continue

    #meng capslock pesan yang diterima
    modifiedMessage = decodeMessage.upper()
    print ("Pesan diterima dari: ", clientAddress, " message: ", decodeMessage)

    #mengirim ke client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

serverSocket.close()
print("socket server telah ditutup.")