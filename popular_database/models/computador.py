from models.utils import generate_id

class Computador:
    def __init__(self, id, modelo, localizacao, status, motivoIndisponibilidade, tipo):
        self.id = id
        self.modelo = modelo
        self.localizacao = localizacao
        self.status = status
        self.motivoIndisponibilidade = motivoIndisponibilidade
        self.tipo = tipo


    @staticmethod
    def create_computadores():
        computadores = {}

        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "1", "Disponivel", "", "Notebook")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "2", "Ocupado", "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "3", "Indisponivel", "Não conecta a internet", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "4", "Indisponivel", "Atualizacao SO", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "5", "Disponivel", "", "Mini PC")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "6", "Disponivel", "", "Mini PC")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "7", "Ocupado", "", "Mini PC")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "8", "Disponivel", "", "Mini PC")
        computadores[computador.id] = computador
        computador = Computador(generate_id(),  "Dell Inspiron", "9", "Disponivel", "", "Mini PC")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "10", "Disponivel", "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "11", "Disponivel", "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "12", "Indisponivel", "Mouse quebrado", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "13", "Ocupado", "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "14", "Disponivel", "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "15", "Disponivel", "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "16", "Disponivel", "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "17", "Indisponivel", "Funciona apenas Windows", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "18", "Ocupado", "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "18", "Ocupado", "", "Desktop")
        computadores[computador.id] = computador

        return computadores


