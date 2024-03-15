from flask import Flask, render_template
from flask_socketio import SocketIO, send

app =Flask(__name__) #Création d'une instance de l'application Flask.
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")#Création d'une instance de SocketIO, associée à l'application Flask.
#permet à n'importe quelle origine d'accéder aux sockets, ce qui est souvent utilisé pour le développement, mais pour une application en production, cela devrait être configuré de manière plus sécurisée.


@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)
    if message != "User connected!":
        send(message, broadcast=True)# Envoi du message à tous les clients connectés, sauf à celui qui a envoyé le message initial.


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host="192.168.106.236")
