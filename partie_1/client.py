import socket

def send_messages(server_host, server_port):
    #Coté client, il faut également créer le socket qui va donner l’accès au serveur :
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Ensuite, il suffit de demander une connexion au serveur (dont on connait le nom d’hôte et le port d’écoute) à l’aide de la méthode .connect():
    client_socket.connect((server_host, server_port))
#la méthode .bind(), coté serveur, qui établit le lien, localement, entre le socket d’écoute et le port de la machine ;
#la méthode .connect(), coté client, envoie une demande de connexion au serveur.

    while True:
        message = input("Entrez votre message (ou 'exit' pour quitter) : ")

        client_socket.send(message.encode())

        if message.lower() == 'exit':
            break

    client_socket.close()

send_messages('127.0.0.1', 3000)
