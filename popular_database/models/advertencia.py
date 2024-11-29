from random import choice


class Advertencia:
    def __init__(self, id, date, motivo, supervisorId, estudanteId):
        self.id = id
        self.date = date
        self.motivo = motivo
        self.supervisorId = supervisorId
        self.estudanteId = estudanteId

    @staticmethod
    def create_motivo():
        return choice(["Uso indevido do computador", "Atraso", "Falta", "Desrespeito aos colegas", "Falando alto", "Tentativa de invasão", "Uso de entorpecentes", "Quebra de regras"])

