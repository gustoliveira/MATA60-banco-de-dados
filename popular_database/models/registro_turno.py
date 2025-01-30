import datetime
from random import choice
from models.utils import generate_id

class RegistroTurno:
    def __init__(self, id, horarioEntrada, horarioSaida, supervisorId):
        self.id = id
        self.horarioEntrada = horarioEntrada
        self.horarioSaida = horarioSaida
        self.supervisorId = supervisorId


    @staticmethod
    def generate_full_log(start_date, end_date, escala):
        registros = {}
        current_date = start_date

        day_number_to_name = {
            0: 'segunda',
            1: 'terca',
            2: 'quarta',
            3: 'quinta',
            4: 'sexta'
        }

        while current_date <= end_date:

            if current_date.weekday() < 5:
                cd = day_number_to_name[current_date.weekday()]

                for turno in ['manha', 'tarde', 'noite']:
                    e = choice([escala[e] for e in escala if escala[e].dia == cd and escala[e].turno == turno])
                    if e is None:
                        break

                    inicio = datetime.datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
                    fim = datetime.datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
                    if turno == 'tarde':
                        inicio = datetime.datetime.now().replace(hour=13, minute=0, second=0, microsecond=0)
                        fim = datetime.datetime.now().replace(hour=17, minute=0, second=0, microsecond=0)
                    if turno == 'noite':
                        inicio = datetime.datetime.now().replace(hour=17, minute=0, second=0, microsecond=0)
                        fim = datetime.datetime.now().replace(hour=20, minute=0, second=0, microsecond=0)

                    registro = RegistroTurno(
                        generate_id(),
                        inicio,
                        fim,
                        e.supervisorId
                    )
                    registros[registro.id] = registro

            current_date += datetime.timedelta(days=1)

        return registros
