import sys
from db import db

class VagaService():

    def listar(self):
        # Retorna a consulta select da classe que manipula o banco.
        return db.DB.select(db.DB, 'estacionamento', '')

    def removerCarro(self, id,dados ):
        # Chama a função edit e retorna a resposta.
        retornoRemoveCarro = db.DB.update(db.DB, 'estacionamento', ['id', id,], dados)        
        return retornoRemoveCarro

    def estacionarCarro(self, dados, id):

        # Chama a função edit e retorna a resposta.
        estacionarCarro = db.DB.edit(db.DB, 'estacionamento', ['id', id], dados)
        return estacionarCarro