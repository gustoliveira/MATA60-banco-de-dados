from models.utils import generate_id, generate_phone_number, cursos_aceitos

class Estudante:
    def __init__(self, id, nome, foto, matricula, curso, email, telefone):
        self.id = id
        self.nome = nome
        self.foto = foto
        self.matricula = matricula
        self.curso = curso
        self.email = email
        self.telefone = telefone


    def __str__(self):
        return f"{self.id}, \"{self.nome}\", \"{self.foto}\", \"{self.matricula}\", \"{self.curso}\", \"{self.email}\", \"{self.telefone}\""


    @staticmethod
    def generate_matricula(fake):
        indice = fake.random_int(min=1, max=2)
        ano = fake.random_int(min=2, max=24)
        semestre = fake.random_int(min=1, max=2)
        curso = fake.random_int(min=100, max=300)
        aluno = fake.random_int(min=10, max=99)
        return f"{indice}{ano}{semestre}{curso}{aluno}"


    @staticmethod
    def generate_email(nome):
        return f"{nome.lower().replace(' ', '_')}@ufba.br"


    @staticmethod
    def generate_file_path(matricula, curso, extension='png'):
        return f"/ufba/alunos/{curso.lower().replace(' ', '_')}/{matricula}/profile/foto.{extension}"


    @staticmethod
    def generate_new_estudante(fake):
        nome = fake.name()
        id = generate_id()
        matricula = Estudante.generate_matricula(fake)
        curso = fake.random_element(cursos_aceitos)
        foto = Estudante.generate_file_path(matricula, curso)
        email = Estudante.generate_email(nome)
        telefone = generate_phone_number()
        return Estudante(id, nome, foto, matricula, curso, email, telefone)


    @staticmethod
    def generate_n_new_estudante(fake, n):
        estudantes = {}

        while len(estudantes) < n:
            estudante = Estudante.generate_new_estudante(fake)
            estudantes[estudante.nome] = estudante

        return estudantes

    
