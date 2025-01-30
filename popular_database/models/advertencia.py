from models.utils import generate_id
from random import choice, random


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

    @staticmethod
    def generate_multiple_adverticies(registros, escala):
        day_number_to_name = {
            0: 'segunda',
            1: 'terca',
            2: 'quarta',
            3: 'quinta',
            4: 'sexta'
        }

        advertencias = {}

        for r in registros:
            if random() > 0.015:  # 1% chance do estudante tomar advertencia
                continue

            turno = 'manha'
            if r.horarioSaida.hour >= 13 and r.horarioSaida.hour <= 17:
                turno = 'tarde'
            if r.horarioSaida.hour >= 17 and r.horarioSaida.hour <= 20:
                turno = 'noite'

            dia = day_number_to_name[r.horarioSaida.weekday()]

            supervisor_id = None
            for e in escala.values():
                if e.dia == dia and e.turno == turno:
                    supervisor_id = e.supervisorId
                    break

            advertencia = Advertencia(
                generate_id(),
                r.horarioSaida,
                Advertencia.create_motivo(),
                supervisor_id,
                r.estudanteId
            )

            advertencias[advertencia.id] = advertencia

        return advertencias
