import datetime
from faker import Faker
from models.estudante import Estudante
from models.supervisor import Supervisor
from models.escala import Escala
from models.computador import Computador
from models.armario import Armario
from models.registro_acesso import RegistroAcesso
from models.registro_turno import RegistroTurno
from models.utils import generate_id
from models.advertencia import Advertencia

fake = Faker()

estudantes = Estudante.generate_n_new_estudante(fake, 500)

supervisores = Supervisor.generate_supervisores_from_estudantes(estudantes, 30)


papeis = {
    'titular': generate_id(),
    'reserva': generate_id(),
    'suplente': generate_id(),
}
escala = Escala.create_escala_completa(supervisores, papeis)
computadores = Computador.create_computadores()
armarios = Armario.create_armarios()

start_date = datetime.datetime.today() - datetime.timedelta(days=360)
end_date = datetime.datetime.today()
registros = RegistroAcesso.generate_full_access_log(estudantes, computadores, armarios, start_date, end_date, supervisores)
registros_turnos = RegistroTurno.generate_full_log(start_date, end_date, escala)
advertencias = Advertencia.generate_multiple_adverticies(registros.values(), escala)

def final(index, length):
    if index == length:
        return ";\n\n"
    return ","

def generate_sql_inserts(estudantes, supervisores, escala, computadores, armarios, registros):
    sql_statements = ['BEGIN;\n\n']

    # Estudantes
    sql_statements.append("INSERT INTO Estudante (Id, Nome, Foto, Matricula, Curso, Email, Telefone) VALUES")
    index = 0
    length = len(estudantes.values())
    for estudante in estudantes.values():
        index = index + 1
        sql_statements.append(f"({estudante.id}, '{estudante.nome}', '{estudante.foto}', '{estudante.matricula}', '{estudante.curso}', '{estudante.email}', '{estudante.telefone}'){final(index, length)}")

    # Armarios
    sql_statements.append("INSERT INTO Armario (Id, Localizacao, Status) VALUES")
    index = 0
    length = len(armarios.values())
    for armario in armarios.values():
        index = index + 1
        sql_statements.append(f"({armario.id}, '{armario.localizacao}', '{armario.status}'){final(index, length)}")

    # Computadores
    sql_statements.append("INSERT INTO Computador (Id, Modelo, Localizacao, Status, MotivoIndisponibilidade, Tipo) VALUES")
    index = 0
    length = len(computadores.values())
    for computador in computadores.values():
        index = index + 1
        sql_statements.append(f"({computador.id}, '{computador.modelo}', '{computador.localizacao}', '{computador.status}', '{computador.motivoIndisponibilidade}', '{computador.tipo}'){final(index, length)}")

    # Papel
    sql_statements.append("INSERT INTO Papel (Id, Descricao) VALUES")
    sql_statements.append(f"({papeis['titular']}, 'titular'),")
    sql_statements.append(f"({papeis['reserva']}, 'reserva'),")
    sql_statements.append(f"({papeis['suplente']}, 'suplente');\n\n")

    # Supervisores
    sql_statements.append("INSERT INTO Supervisor (Id, IdEstudante) VALUES")
    index = 0
    length = len(supervisores.values())
    for supervisor in supervisores.values():
        index = index + 1
        sql_statements.append(f"({supervisor.id}, {supervisor.estudanteId}){final(index, length)}")

    # Escala
    sql_statements.append("INSERT INTO Escala (Id, HorarioInicio, HorarioSaida, Dia, IdPapel, IdSupervisor) VALUES")
    index = 0
    length = len(escala.values())
    for e in escala.values():
        index = index + 1
        inicio = datetime.datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
        fim = datetime.datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
        if e.turno == 'tarde':
            inicio = datetime.datetime.now().replace(hour=13, minute=0, second=0, microsecond=0)
            fim = datetime.datetime.now().replace(hour=17, minute=0, second=0, microsecond=0)
        if e.turno == 'noite':
            inicio = datetime.datetime.now().replace(hour=17, minute=0, second=0, microsecond=0)
            fim = datetime.datetime.now().replace(hour=20, minute=0, second=0, microsecond=0)

        sql_statements.append(f"({e.id}, '{inicio}', '{fim}', '{e.dia}', {e.papel}, {e.supervisorId}){final(index, length)}")

    # Registros de Acesso
    sql_statements.append("INSERT INTO RegistroAcesso (Id, HorarioInicio, HorarioSaida, IdArmario, IdComputador, IdEstudante) VALUES")
    index = 0
    length = len(registros.values())
    for registro in registros.values():
        index = index + 1
        sql_statements.append(f"({registro.id}, '{registro.horarioInicio}', '{registro.horarioSaida}', {registro.armarioId}, {registro.computadorId}, {registro.estudanteId}){final(index, length)}")


    # Registros de Turno
    sql_statements.append("INSERT INTO RegistroTurno (Id, HorarioEntrada, HorarioSaida, IdSupervisor) VALUES")
    index = 0
    length = len(registros_turnos.values())
    for registro in registros_turnos.values():
        index = index + 1
        sql_statements.append(f"({registro.id}, '{registro.horarioEntrada}', '{registro.horarioSaida}', {registro.supervisorId}){final(index, length)}")


    # Advertencias
    sql_statements.append("INSERT INTO Advertencia (Id, Data, Motivo, EstudanteId, SupervisorId) VALUES")
    index = 0
    length = len(advertencias.values())
    for advertencia in advertencias.values():
        index = index + 1
        sql_statements.append(f"({advertencia.id}, '{advertencia.date}', '{advertencia.motivo}', {advertencia.estudanteId}, {advertencia.supervisorId}){final(index, length)}")



    sql_statements.append('COMMIT;')
    return "\n".join(sql_statements)


sql_inserts = generate_sql_inserts(estudantes, supervisores, escala, computadores, armarios, registros)

print(sql_inserts)
