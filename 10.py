from datetime import datetime, date
class Pessoa():
    def __init__(self, nome, genero, data_nascimento, data_entrada):
        self.nome = nome
        self.genero = genero
        self.data_nascimento = data_nascimento
        self.data_entrada = data_entrada
class Professor(Pessoa):
    def __init__(self, nome, genero, data_nascimento, data_entrada, area_formacao):
        super(). __init__(nome, genero, data_nascimento, data_entrada)
        self.area_formacao = area_formacao
class Aluno(Pessoa):
    def __init__(self, nome, genero, data_nascimento, data_entrada, historico):
        super(). __init__(nome, genero, data_nascimento, data_entrada)
        self.historico = historico
class Prova():
    def __init__(self, data_hora, tipo, nota):
        self.data_hora = data_hora
        self.tipo = tipo
        self.nota = nota
class Disciplina():
    def __init__(self, nome, descricao, ementa):
        self.nome = nome
        self.descricao = descricao
        self.ementa = ementa