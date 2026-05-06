
#menerima balasan dari server
modified_message, serverAddress = clientSocket.recvfrom(2048)
print("pesan diterima dari: ", )
print(modified_message.decode())
