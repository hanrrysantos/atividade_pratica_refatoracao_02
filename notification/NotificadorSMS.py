from interface.INotificador import INotificador

class NotificadorSMS(INotificador):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[SMS] Enviando SMS para {destinatario}: '{mensagem}'")