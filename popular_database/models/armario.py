from models.utils import generate_id

class Armario:
    def __init__(self, id, localizacao, status):
        self.id = id
        self.localizacao = localizacao
        self.status = status

    @staticmethod
    def create_armarios():
        armarios = {}

        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
            for j in range(1, 2):
                armario = Armario(generate_id(), f"{i}-0{j}", False)
                armarios[armario.id] = armario

        return armarios

