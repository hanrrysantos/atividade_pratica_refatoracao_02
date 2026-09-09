from typing import List, Dict
from interface.IVendaRepository import IVendaRepository

class VendaMemoriaRepository(IVendaRepository):
    def __init__(self):
        # Lista em memória simulando uma tabela do banco
        self.vendas: List[Dict[str, float]] = []

    def salvar(self, cliente: str, valor: float) -> None:
        self.vendas.append({"cliente": cliente, "valor": valor})
        print(f"[BD/Memória] Venda de R$ {valor:.2f} salva na RAM para {cliente}. Total de registros: {len(self.vendas)}")