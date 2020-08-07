#Importa as libs
import platform #Lib que reconhece o sistema operacional
import os       #Lib que possui recursos do sistema operacional
import sys
import time
from db import db
from pyfiglet import Figlet #Lib para criar interface mais elaborada

from service import VagaService


class Cadastros():

    def __init__(self):
        self.menu()

    #Função para limpar console de acordo com sistema operacional
    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')


    def zerarDados(self):
        dados = {}
        dados ['id'] = id
        dados['vaga'] = 'Vaga ' + dados ['id']
        dados['carro'] = ''
        dados ['status'] = '0'

        vagaService = VagaService.VagaService
        retorno = vagaService.removerCarro(vagaService, id, dados)


    def menu(self):        
        while 1:
            self.clear()                    
            print('# Vagas de Estacionamento #')
            print('')
            menuPrincipal = [' VAGAS',' VAGAS DISPONÍVEIS',' ESTACIONAR CARRO',' REMOVER CARRO ESTACIONADO',' RESUMO DE VAGAS',' SAIR']
            items = 1
            for mp in menuPrincipal:
                print( str(items) + ' - ' + mp)
                items = items + 1
            print('')
            opcoesPrincipal = int(input('Selecione a operação: '))
            print('')

            #LISTAR TODAS AS VAGAS OCUPADAS OU NAO
            if opcoesPrincipal == 1:
                self.clear()                                
                print('# LISTA DE VAGAS #')
                print('')
                menuListar = ['VAGAS', 'VOLTAR AO MENU']
                items = 1
                for mListar in menuListar:
                    print(str(items) + ' - ' + mListar)
                    items = items + 1
                print('')
                listarOP = int(input('Operação: '))
                print('')
                if listarOP == 1:
                    print('LISTA DE VAGAS')

                    vagasService = VagaService.VagaService
                    vagas = vagasService.listar(vagasService)

                    if (vagas):
                        self.clear()
                        print('------------------')
                        for vaga in vagas:
                            print('ID: '+ vaga['id'])
                            print('\nVaga: '    + vaga['vaga'])
                            print('\nCarro: '   + vaga['carro'])
                            print('\nStatus: '  + 'Livre' if vaga['status'] == '0' else 'Ocupada')
                            print('------------------')

                    input(str('\nDigite algo para continuar...\n'))

                else:
                    print('Finalizando Operação de Listagem.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)

            #LISTAR APENAS AS VAGAS LIVRES
            elif opcoesPrincipal == 2:
                self.clear()                                
                print('# LISTA DE VAGAS #')
                print('')
                menuListar = ['VAGAS', 'VOLTAR AO MENU']
                items = 1
                for mListar in menuListar:
                    print(str(items) + ' - ' + mListar)
                    items = items + 1
                print('')
                listarOP = int(input('Operação: '))
                print('')
                if listarOP == 1:
                    print('LISTA DE VAGAS')

                    vagasService = VagaService.VagaService
                    vagasDisponiveis = vagasService.listar(vagasService)

                    if (vagasDisponiveis):
                        self.clear()
                        print('------------------')
                        for vaga in vagasDisponiveis:
                            if vaga['status'] == '0':
                                print('ID: '+ vaga['id'])
                                print('\nVaga: '    + vaga['vaga'])
                                print('\nCarro: '   + vaga['carro'])
                                print('\nStatus: '  + 'Livre' if vaga['status'] == '0' else 'Ocupada')
                                print('------------------')
                            
                    input(str('\nDigite algo para continuar...\n'))

                else:
                    print('Finalizando Operação de Listagem.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)

            #ESTACIONAR CARRO
            elif opcoesPrincipal == 3:
                self.clear()                                
                print('# ESTACIONAR CARRO #')
                print('')
                menuEditar = ['ESTACIONAR', 'VOLTAR AO MENU']
                items = 1
                for mEditar in menuEditar:
                    print(str(items) + ' - ' + mEditar)
                    items = items + 1
                print('')
                editarOP = int(input('Operação: '))
                print('')
                if editarOP == 1:
                    print('ESTACIONAR CARRO.')

                    id = input(str('Digite o ID da vaga que deseja estacionar:'))

                    print('\n Aguarde estamos estacionando seu carro... ' + id + '\n')

                    dados = {}
                    dados['id'] = id 
                    dados['vaga'] = input('Numero da vaga: ')
                    dados['carro'] = input('Nome do carro: ')
                    dados['status'] = input('Status: (0 - Livre e 1 - Ocupado) ')                    

                    vagaService = VagaService.VagaService
                    retorno = vagaService.estacionarCarro(vagaService, dados, id)

                    if retorno:
                        print('Carro estacionado!')
                    else:
                        print('Não foi possivel estacionar o seu carro!')

                else:
                    print('Finalizando Operação Estacionar.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)

            #REMOVER CARRO DA VAGA
            elif opcoesPrincipal == 4:
                self.clear()                
                print(' # REMOVER CARRO DA VAGA #')
                print('')
                menuExcluir = ['REMOVER', 'VOLTAR AO MENU']
                items = 1
                for mExcluir in menuExcluir:
                    print(str(items) + ' - ' + mExcluir)
                    items = items + 1
                print('')
                excluirOP = int(input('Operação: '))
                print('')
                if excluirOP == 1:
                    id      = str(input('Digite o ID do carro que deseja remover:'))                                                            

                    dados = {}
                    dados['id'] = id
                    dados['vaga'] = 'Vaga ' + dados ['id']
                    dados['carro'] = ''
                    dados['status'] = '0'

                    vagaService = VagaService.VagaService
                    retorno = vagaService.removerCarro(vagaService, id, dados)

                    if retorno:
                        print('Carro removido com sucesso!')
                    else:
                        print('Erro ao remover carro!')
                    time.sleep(1)
                else:
                    print('Finalizando Operação de Exclusão.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)

            #RESUMO DAS VAGAS
            elif opcoesPrincipal == 5:
                cont = 0
                cont2 = 0
                self.clear()                
                print(' # RESUMO DAS VAGAS#')
                print('')
                menuExcluir = ['RESUMO', 'VOLTAR AO MENU']
                items = 1
                for mExcluir in menuExcluir:
                    print(str(items) + ' - ' + mExcluir)
                    items = items + 1
                print('')
                excluirOP = int(input('Operação: '))
                print('')

                vagasService = VagaService.VagaService
                vagas = vagasService.listar(vagasService)

                if (vagas):
                    self.clear()
                    print('------------------')
                    for vaga in vagas:
                        if vaga['status'] == '0':
                            cont += 1                            
                        else:    
                            cont2 += 1                            

                    print('\n Vagas Livres: {}'.format(cont) )
                    print('------------------')
                    print('\n Vagas Ocupada: {}'.format(cont2) )
                    print('------------------')
                    input(str('\nDigite algo para continuar...\n'))

                else:
                    print('Finalizando Operação de Listagem.')
                    time.sleep(1)
                    print('Obrigado por utilizar nossos serviços.')
                    time.sleep(0.8)
                
            elif opcoesPrincipal == 6:
                i = ' '
                print('')
                print('Finalizando Sistema', '')
                time.sleep(1)

                for p in range(5):
                    print(i)
                    time.sleep(0.5)

                print('Obrigado por utilizar nossos serviços.')
                print('')                
                time.sleep(0.8)
                break

            else:
                print('Operação não existe, tente novamente!')
                time.sleep(1.5)
                self.clear()
