import json
import os

# Classe responsável por manipular o  nosso sistema
# de arquivos.
class DB():

    # Função que retorna o caminho do arquivo
    # com base no nome da tabela.
    #
    # Exemplo: Parâmetro = 'usuario'
    # Retorno: '/usuarioqualquer/sistema-bancario/db/usuario.json'
    def getJSON(self, tabela):

        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, tabela + '.json')

        return filename

    # Função que faz um "select" nos arquivos de banco.
    # Recebemos por parâmetro o nome da tabela (usuario ou conta)
    # que representa o nome do arquivo.
    #
    # O segundo parâmetro é uma implementação simples de um "where".
    # Caso venha vazio, é retornado todos os registros do arquivo
    # especificado. Caso contrário é aplicado um filtro.
    #
    # Exemplo de WHERE: ['id','250']
    # Se a tabela for usuario, irá buscar um usuário que contenha
    # o campo 'id' com valor de '250'.
    def select(self, tabela, where):
        # Pega o nome do arquivo.
        filename = self.getJSON(self, tabela)

        # Abre o arquivo
        with open(filename) as file:
            # Carrega o conteúdo do arquivo em uma variável.
            vaga = json.load(file)

            # Se não tiver where, retorna todos os registros.
            if len(where) == 0:
                return vaga[tabela]
            # Se tiver um where
            elif len(where) == 2:
                # Percorre todos os itens do arquivo
                for estacionamento in vaga[tabela]:

                    # Verifica pela chave e valor se algum registro bate
                    if estacionamento[where[0]] == where[1]:
                        # Se sim ele é retornado
                        return estacionamento


    # Função para editar um registro nos arquivos.
    # Recebemos o nome de um arquivo por parâmetro, um filtro Where
    # (Seguindo o exemplo do select) para saber qual registro editar,
    # e os novos valores
    def edit(self, tabela, where, valores):
        # Pega o nome do arquivo.
        filename = self.getJSON(self, tabela)
        # Abre o arquivo
        with open(filename) as file:
            # Carrega o arquivo em uma variável
            estacionamento = json.load(file)
            # Pega o tamanho do arquivo para usar em um laço.
            length = len(estacionamento[tabela])
            # Para cada item existente
            for row in range(length):
                # Verifica se o campo bate com o valor do where
                if estacionamento[tabela][row][where[0]] == str(where[1]):
                    # Seta os novos dados recebidos
                    estacionamento[tabela][row] = valores
            # Abre o arquivo com permissão de escrita
            with open(filename, 'w') as file:
                # Salva o novo arquivo atualizado
                json.dump(estacionamento, file, indent=4)
        # Retorno
        return True