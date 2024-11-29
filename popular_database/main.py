from faker import Faker
from models.estudante import Estudante
from models.supervisor import Supervisor
from models.escala import Escala
from models.computador import Computador
from models.armario import Armario

fake = Faker()

estudantes = Estudante.generate_n_new_estudante(fake, 5)

supervisores = Supervisor.generate_supervisores_from_estudantes(estudantes, 2)

escala = Escala.create_escala_completa(supervisores)
computadores = Computador.create_computadores()
armarios = Armario.create_armarios()

print("\nEstudantes (id, nome, foto, matricula, curso, email, telefone)")
for estudante in estudantes.values():
    print(estudante)

print("\nSupervisores (id, estudanteId)")
for supervisor in supervisores.values():
    print(supervisor)

