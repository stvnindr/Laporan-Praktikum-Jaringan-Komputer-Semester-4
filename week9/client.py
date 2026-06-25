from socket import *
import sys

serverName = 'localhost'
serverPort = 6789

if len(sys.argv) < 2:
    print("Cara penggunaan: python client.py <nama_file>")
    sys.exit()

filename = sys.argv[1]

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    
    httpRequest = f"GET /{filename} HTTP/1.1\r\nHost: {serverName}\r\n\r\n"
    clientSocket.send(httpRequest.encode())
    
    print(f"--- Mengirim permintaan untuk file: {filename} ---")
    print("--- Menerima Respons dari Server ---\n")
    
    response = ""
    while True:
        data = clientSocket.recv(1024).decode()
        if not data:
            break
        response += data
        
    print(response)

except ConnectionRefusedError:
    print("Error: Tidak dapat terhubung ke server. Pastikan server.py sudah dijalankan.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
finally:
    clientSocket.close()