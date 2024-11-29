import random
from models.utils import generate_id

class Supervisor:
    def __init__(self, id, estudanteId, nome):
        self.id = id
        self.estudanteId = estudanteId
        self.nome = nome

    # TODO: Implementar o método __string__ para a classe Supervisor
    def __str__(self):
        return f"{self.id}, {self.estudanteId}"




    @staticmethod
    def generate_supervisores_from_estudantes(estudantes, qntdSupervisores):
        supervisores = {}

        while len(supervisores) < qntdSupervisores:
            _, estudante = random.choice(list(estudantes.items()))
            supervisor = Supervisor(generate_id(), estudante.id, estudante.nome)
            supervisores[estudante.nome] = supervisor

        return supervisores

