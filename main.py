from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Criar aplicação e socketio
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Criação da 1º rota
@app.route("/")
def homepage(): # Criação da função
    return render_template("homepage.html")

#Funcionalidade de enviar mensagem

@socketio.on("message") #Usamos o evento message para mensagens
def conversa(mensagem): # Recebe como parametro uma mensagem
    send(mensagem, broadcast=True) #Broadcast envia a mensagem para todos os conectados no túnel


# Roda a aplicação
socketio.run(app, host="xx.168.xx.xx")
