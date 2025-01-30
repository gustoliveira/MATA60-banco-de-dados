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

        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "1", False, "", "Notebook")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "2", False, "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "3", False, "Não conecta a internet", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "4", False, "Atualizacao SO", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "5", False, "", "Mini PC")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "6", False, "", "Mini PC")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "7", False, "", "Mini PC")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "HP EliteDesk 800 G4 - Mini PC", "8", False, "", "Mini PC")
        computadores[computador.id] = computador
        computador = Computador(generate_id(),  "Dell Inspiron", "9", False, "", "Mini PC")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "10", False, "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "11", False, "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "12", False, "Mouse quebrado", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "13", False, "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "14", False, "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "15", False, "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "16", False, "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "17", False, "Funciona apenas Windows", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "18", False, "", "Desktop")
        computadores[computador.id] = computador
        computador = Computador(generate_id(), "Dell Inspiron", "18", False, "", "Desktop")
        computadores[computador.id] = computador

        return computadores


