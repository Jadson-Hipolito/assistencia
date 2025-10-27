class Cargo:
    def __init__(self, id_cargo, nome_cargo):
        self.id_cargo = id_cargo
        self.nome_cargo = nome_cargo

    def __repr__(self):
        return f"Cargo(id={self.id_cargo}, nome={self.nome_cargo})"

