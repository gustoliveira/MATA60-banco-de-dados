import datetime
from faker import Faker
from models.estudante import Estudante
from models.supervisor import Supervisor
from models.escala import Escala
from models.computador import Computador
from models.armario import Armario
from models.registro_acesso import RegistroAcesso

fake = Faker()

estudantes = Estudante.generate_n_new_estudante(fake, 100)

supervisores = Supervisor.generate_supervisores_from_estudantes(estudantes, 1)

escala = Escala.create_escala_completa(supervisores)
computadores = Computador.create_computadores()
armarios = Armario.create_armarios()

print("Estudantes (id, nome, foto, matricula, curso, email, telefone)")
index = 1
for estudante in estudantes.values():
    print(f"{index} - {estudante}")
    index = 1 + index
print("\n")

index = 1
print("Supervisores (id, estudanteId)")
for supervisor in supervisores.values():
    print(f"{index} - {supervisor}")
    index = 1 + index
print("\n")

print("Escala (id, dia, turno, supervisorId, papel)")
for e in escala.values():
    print(e)
print("")

print("Registro de horarios")
yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
today = datetime.datetime.today()
registros = RegistroAcesso.generate_full_access_log(estudantes, computadores, armarios, yesterday, today)
for registro in registros.values():
    print(f"{registro}\n")

