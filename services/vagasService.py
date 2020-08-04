import os
import time
from views import menuViews

class vagasService:

    def vagas():

        while(1):
            limp = menuViews
            limp.limpar()

            listaVagas = {
                "vaga01": "livre",
                "vaga02": "livre",
                "vaga03": "livre",
                "vaga04": "livre",
                "vaga05": "livre"
            }
            
            print('####### VAGAS ########')
            print(listaVagas)

            print('')
            print('0 - VOLTAR AO MENU.')

            op_vagas = int(input('Escolha uma opcao: '))        

            if(op_vagas == 0):
                print('Voltando ao menu principal')
                time.sleep(0.5)
                break       
            else:
                print('Opção não existe.')
                time.sleep(0.5)
                limp.limpar()

    def vagasDisponiveis():
        while(1):

            limp = menuViews
            limp.limpar()
            print('####### VAGAS DISPONÍVEIS ########')
            print('')
            print('0 - VOLTAR AO MENU.')

            op = int(input('Escolha uma opcao: '))

            if(op == 0):
                print('Voltando ao menu principal')
                time.sleep(0.5)
                break
            else:
                print('Opção não existe.')
                time.sleep(0.5)
                limp.limpar()

    def estacionarCarro():
        while(1):
            limp = menuViews
            limp.limpar()
            print('####### ESTACIONAR CARRO ########')
            time.sleep(1)

            print('1 - SELECIONAR UMA VAGA.')        
            print('0 - VOLTAR AO MENU.')

            op_estacionar = int(input('Escolha uma opcao: '))   

            if (op_estacionar == 1):
                print('Vaga {} selecionada. '.format(op_estacionar))
                time.sleep(1)
                break                
            if(op_estacionar == 0):
                print('Voltando ao menu principal')
                time.sleep(0.5)
                break           
            else:
                print('Opção não existe.')
                time.sleep(0.5)
                limp.limpar()

    def removerCarro():
        while(1):
            limp = menuViews
            limp.limpar()
            print('####### REMOVER CARRO ########')
            
            print('1 - REMOVER UMA VAGA.')        
            print('0 - VOLTAR AO MENU.')

            op = int(input('Escolha uma opcao: '))   

            if(op == 1):
                print('Vaga {} removida. '.format(op))
                time.sleep(0.5)
                break
            elif(op == 0):
                print('Voltando ao menu principal')
                time.sleep(0.5)
                break
            else:
                print('Opção não existe.')
                time.sleep(0.5)
                limp.limpar()
       


    def resumoEstacionamento():
        while(1):
            limp = menuViews.limpar()
            print('####### RESUMO DE VAGAS ########')

            op = int(input('Escolha uma opcao: '))

            if(op == 1):
                print('RESUMO. '.format(op))
                break
            elif(op == 0):
                print('Voltando ao menu principal')
                time.sleep(0.5)
                break
            else:
                print('Opção não existe.')
                time.sleep(0.5)
                limp.limpar()