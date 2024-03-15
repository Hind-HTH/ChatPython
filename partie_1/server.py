import socket

def start_server(host, port):
    #Création d’un objet socket :
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #la famille d’adresses : socket.AF_INET = adresses Internet de type IPv4 ;
    #le type du socket : socket.SOCK_STREAM = protocole TCP.



    server_socket.bind((host, port))

    server_socket.listen()
    print(f"Serveur en attente de connexions sur {host}:{port}")

    while True:
    #Lorsqu’un client se connecte, le serveur est sensé accepter la connexion, avec la méthode .accept():
        client_socket, client_address = server_socket.accept()
        #adresse_client : l’adresse du client.
        print(f"Connexion établie avec {client_address}")

        while True:
            
            data = client_socket.recv(1024)
            # if not data:
            #     print(f"Client {client_address} s'est déconnecté.")
            #     break  
           
            if data.decode().lower() == 'exit':
                print(f"Client {client_address} a quitté la session.")
                break
            print(f"Client dit : {data.decode()}")

        client_socket.close()

    server_socket.close()

start_server('127.0.0.1', 3000)
