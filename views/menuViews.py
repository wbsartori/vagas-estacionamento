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
        op = int(input('Escolha uma opcao: '))

        if( op == 1):            
            vagas = vagasService.vagasService.vagas()

        elif( op == 2):            
            vagas = vagasService.vagasService.vagasDisponiveis()

        elif( op == 3):            
            vagas = vagasService.vagasService.estacionarCarro()

        elif( op == 4):            
            vagas = vagasService.vagasService.removerCarro()

        elif( op == 5):            
            vagas = vagasService.vagasService.resumoEstacionamento()

        elif( op == 0):            
            print('Obrigado por usar nosso sistema.')
            time.sleep(2)
            break

        else:
            print('Opção não existe.')
            time.sleep(1)