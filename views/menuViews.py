import os 
import platform
import sys
import time
from services import vagasService

def limpar():
    if (platform.system() == 'Windows'):
        os.system('cls')
    else:    
        os.system('clear')
 

def menuPrincipal():    
    while(1):
        limpar()    
        print('######## ESTACIONAMENTO ##########')
        print('1 - VAGAS.')        
        print('2 - VAGAS DISPONÍVEIS.')
        print('3 - ESTACIONAR CARRO.')
        print('4 - REMOVER CARRO ESTACIONADO.')
        print('5 - RESUMO DE VAGAS.')
        print('0 - SAIR.')
        print('')
        opcao = int(input('Escolha uma opcao: '))

        if( opcao == 1):            
            vagas = vagasService.vagasService
            vagas.vagas()

        elif( opcao == 2):            
            vagas = vagasService.vagasService
            vagas.vagasDisponiveis()
        elif( opcao == 3):            
            vagas = vagasService.vagasService
            vagas.estacionarCarro()

        elif( opcao == 4):            
            vagas = vagasService.vagasService
            vagas.removerCarro()

        elif( opcao == 5):            
            vagas = vagasService.vagasService
            vagas.resumoEstacionamento()

        elif( opcao == 0):            
            print('Obrigado por usar nosso sistema.')
            time.sleep(0.5)
            break

        else:
            print('Opção não existe.')
            time.sleep(1)