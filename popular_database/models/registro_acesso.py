from models.utils import generate_id, generate_time_manha, generate_time_tarde
import random
import datetime

class RegistroAcesso:
    def __init__(self, id, horarioInicio, horarioSaida, armarioId, computadorId, estudanteId):
        self.id = id
        self.horarioInicio = horarioInicio
        self.horarioSaida = horarioSaida
        self.armarioId = armarioId
        self.computadorId = computadorId
        self.estudanteId = estudanteId

    def __str__(self):
        armario = self.armarioId
        if self.armarioId == None:
            armario = "Null"

        return f"id: {self.id}\n\tEntrada: \"{self.horarioInicio}\", Saida: \"{self.horarioSaida}\",\n\tArmarioId: {armario}, ComputadorId: {self.computadorId}, EstudanteId: {self.estudanteId}"


    @staticmethod
    def generate_full_access_log(estudantes, computadores, armarios, start_date, end_date):
        registros = {}
        current_date = start_date
        occupied_computers = {}
        occupied_armarios = {}

        while current_date <= end_date:
            if current_date.weekday() < 5:  # Segunda a Sexta
                for turno in ['manha', 'tarde']:
                    available_students = list(estudantes.values())
                    random.shuffle(available_students)
                    
                    for estudante in available_students:
                        if random.random() < 0.2:  # 20% chance do estudante ir para o laboratório
                            available_computers = [c for c in computadores.values() if c.id not in occupied_computers]

                            if not available_computers:
                                continue
                            
                            computador = random.choice(available_computers)
                            available_armarios = [a for a in armarios.values() if a.id not in occupied_armarios]
                            armario = random.choice(available_armarios) if available_armarios else None

                            if turno == 'manha':
                                horario_inicio = generate_time_manha(current_date)
                                horario_saida = generate_time_manha(current_date)
                                max_duration = datetime.timedelta(hours=4)  # Turnos de no máximo 4 horas
                            else:
                                horario_inicio = generate_time_tarde(current_date)
                                horario_saida = generate_time_tarde(current_date)
                                max_duration = datetime.timedelta(hours=7)  # Turnos de no máximo 7 horas

                            # Garanta que horario_saida seja após horario_inicio e dentro da duração máxima
                            randon_minutes = random.randint(15, 59)
                            horario_saida = max(horario_saida, horario_inicio + datetime.timedelta(minutes=randon_minutes))
                            horario_saida = min(horario_saida, horario_inicio + max_duration)

                            registro = RegistroAcesso(
                                generate_id(),
                                horario_inicio,
                                horario_saida,
                                armario.id if armario else "NULL",
                                computador.id,
                                estudante.id
                            )

                            registros[registro.id] = registro
                            occupied_computers[computador.id] = (horario_inicio, horario_saida)
                            if armario:
                                occupied_armarios[armario.id] = (horario_inicio, horario_saida)

                    current_time = datetime.datetime.combine(current_date, datetime.time(12, 0) if turno == 'manha' else datetime.time(20, 0))
                    occupied_computers = {k: v for k, v in occupied_computers.items() if v[1] > current_time}
                    occupied_armarios = {k: v for k, v in occupied_armarios.items() if v[1] > current_time}

            current_date += datetime.timedelta(days=1)

        return registros

