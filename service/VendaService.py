from interface.IVendaRepository import IVendaRepository
from interface.INotificador import INotificador

class VendaService:
    def __init__(self, repository: IVendaRepository, notificador: INotificador):
        self.repository = repository
        self.notificador = notificador

    def executar_venda(self, cliente: str, valor: float, destinatario_notificacao: str) -> float:
        if valor <= 0:
            raise ValueError("Valor inválido")

        valor_com_desconto = valor * 0.9 if valor > 100 else valor
        self.repository.salvar(cliente, valor_com_desconto)
        
        mensagem = f"Olá {cliente}, sua compra no valor de R$ {valor_com_desconto:.2f} foi realizada com sucesso!"
        self.notificador.enviar(destinatario_notificacao, mensagem)

        return valor_com_desconto