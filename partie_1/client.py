import socket

def send_messages(server_host, server_port):
    # Crée un socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Se connecte au serveur
    client_socket.connect((server_host, server_port))

    while True:
        message = input("Entrez votre message (ou 'exit' pour quitter) : ")

        # Envoie le message au serveur
        client_socket.send(message.encode())

        if message.lower() == 'exit':
            break

        # Reçoit la réponse du serveur
        # data = client_socket.recv(1024)
        # print(f"Serveur dit : {data.decode()}")

    # Ferme la connexion
    client_socket.close()

# Utilisation de la fonction
send_messages('127.0.0.1', 3000)
