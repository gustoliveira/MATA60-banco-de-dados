import uuid
import random


status = ["Disponivel", "Ocupado", "Indisponivel"]


cursos_aceitos = ["Ciência da Computação", "Engenharia de Software", "Sistemas de Informação", "Bacharelado Interdisciplinar de Ciência e Tecnologia"]


def generate_id():
    return int(str(uuid.uuid4().int)[:10])


def generate_phone_number():
    ddds = [11, 21, 31, 41, 51, 61, 71, 81, 85, 91, 95, 96, 98, 73, 74, 75, 77]
    weights = [10, 5, 3, 2, 2, 1, 70, 1, 1, 1, 1, 1, 1, 7, 3, 3, 2]
    ddd = random.choices(ddds, weights=weights, k=1)[0]
    return f"({ddd}) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

