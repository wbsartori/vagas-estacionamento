import time
from views import menuViews

class vagasService():

    def vagas():
        limp = menuViews.limpar()
        print('####### VAGAS ########')
        time.sleep(1)

    def vagasDisponiveis():
        limp = menuViews.limpar()
        print('####### VAGAS DISPONÍVEIS ########')
        time.sleep(1)

    def removerCarro():
        limp = menuViews.limpar()
        print('####### REMOVER CARRO ########')
        time.sleep(1)

    def estacionarCarro():
        limp = menuViews.limpar()
        print('####### ESTACIONAR CARRO ########')
        time.sleep(1)

    def resumoEstacionamento():
        limp = menuViews.limpar()
        print('####### RESUMO DE VAGAS ########')
        time.sleep(1)