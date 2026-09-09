from interface.INotificador import INotificador

class NotificadorEmail(INotificador):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[E-mail] Enviando para {destinatario}: '{mensagem}'")