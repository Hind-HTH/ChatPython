import socket

def start_server(host, port):
    # Crée un socket serveur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #  socket à  IP et un port
    server_socket.bind((host, port))

    # Écoute les connexions entrantes
    server_socket.listen()
    print(f"Serveur en attente de connexions sur {host}:{port}")

    while True:
        # Accepte la connexion d'un client
        client_socket, client_address = server_socket.accept()
        print(f"Connexion établie avec {client_address}")

        while True:
            # Échange d'informations avec le client
            data = client_socket.recv(1024)
            if not data:
                print(f"Client {client_address} s'est déconnecté.")
                break  # Si le client se déconnecte, sort de la boucle
            print(f"Client dit : {data.decode()}")

            # Vérifie si le client a envoyé "exit"
            if data.decode().lower() == 'exit':
                print(f"Client {client_address} a quitté la session.")
                break

        # Ferme la connexion avec le client
        client_socket.close()

    # Ferme le socket serveur
    server_socket.close()

# Utilisation de la fonction
start_server('127.0.0.1', 3000)
