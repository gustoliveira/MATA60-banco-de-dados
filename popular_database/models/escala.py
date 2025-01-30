from random import choice
from models.utils import generate_id


class Escala:
    def __init__(self, id, dia, turno, supervisorId, papel):
        self.id = id
        self.supervisorId = supervisorId
        self.dia = dia
        self.turno = turno
        self.papel = papel


    def __str__(self):
        return f"{self.id}, {self.supervisorId}, \"{self.dia}\", \"{self.turno}\", \"{self.papel}\""


    @staticmethod
    def create_escala_completa(supervisores, papeis):
        escala = {}

        for dia in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
            for turno in ['manha', 'tarde', 'noite']:
                for papelId in papeis.values():
                    supervisor = choice(list(supervisores.values()))
                    id = generate_id()
                    escala[id] = Escala(id, dia, turno, supervisor.id, papelId)

        return escala

