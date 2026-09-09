from interface.IVendaRepository import IVendaRepository

class VendaArquivoRepository(IVendaRepository):
    def salvar(self, cliente: str, valor: float) -> None:
        with open("vendas.txt", "a", encoding="utf-8") as f:
            f.write(f"{cliente};{valor}\n")
        print(f"[BD/Arquivo] Venda de R$ {valor:.2f} salva no arquivo para {cliente}.")