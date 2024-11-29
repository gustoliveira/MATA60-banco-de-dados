from random import choice
from models.utils import generate_id


class Escala:
    def __init__(self, id, dia, turno, supervisorId, papel):
        self.id = id
        self.supervisorId = supervisorId
        self.dia = dia
        self.turno = turno
        self.papel = papel


    @staticmethod
    def create_escala_completa(supervisores):
        escala = {}

        for dia in ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']:
            for turno in ['Manhã', 'Tarde', 'Noite']:
                for papel in ['Titular', 'Reserva', 'Suplente']:
                    supervisor = choice(list(supervisores.values()))
                    id = generate_id()
                    escala[id] = Escala(id, dia, turno, supervisor.id, papel)

        return escala

