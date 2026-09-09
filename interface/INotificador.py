from abc import ABC, abstractmethod

class INotificador(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str) -> None:
        """Envia uma notifacção para o destinatário."""
        pass