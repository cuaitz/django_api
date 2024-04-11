from channels.generic.websocket import WebsocketConsumer

class EchoWSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        print(f"Mensagem recebida: {text_data}")
        self.send(text_data)
