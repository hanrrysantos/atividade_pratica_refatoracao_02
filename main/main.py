from repository.VendaArquivoRepository import VendaArquivoRepository
from repository.VendaMemoriaRepository import VendaMemoriaRepository
from notification.NotificadorEmail import NotificadorEmail
from notification.NotificadorSMS import NotificadorSMS
from service.VendaService import VendaService

if __name__ == "__main__":
    repo_arquivo = VendaArquivoRepository()
    notificador_email = NotificadorEmail()

    venda_service_1 = VendaService(repository=repo_arquivo, notificador=notificador_email)
    venda_service_1.executar_venda(
        cliente="Ana Silva", 
        valor=150.0, 
        destinatario_notificacao="ana@gmail.com"
    )

    print("\n")

    repo_memoria = VendaMemoriaRepository()
    notificador_sms = NotificadorSMS()

    venda_service_2 = VendaService(repository=repo_memoria, notificador=notificador_sms)
    venda_service_2.executar_venda(
        cliente="Carlos Souza", 
        valor=80.0, 
        destinatario_notificacao="+55 94 9 9999-9999"
    )