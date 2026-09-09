from abc import ABC, abstractmethod

class IVendaRepository(ABC):
    @abstractmethod
    def salvar(self, cliente: str, valor: float) -> None:
        """Salva os dados da venda na camada de persistência."""
        pass

