from assistencia_tecnica.models.cliente import Cliente
from assistencia_tecnica.validadores import validar_nome, validar_endereco, validar_contato, validar_cpf

def listar_clientes():
    return [c.to_dict() for c in Cliente.listar_todos()]

def obter_cliente(id_cliente: int):
    cliente = Cliente.consultar(id_cliente)
    return cliente.to_dict() if cliente else None

def criar_cliente(data: dict):
    nome = data.get("nome")
    endereco = data.get("endereco")
    contato = data.get("contato")
    cpf = data.get("cpf")

    # Validações
    if not validar_nome(nome):
        raise ValueError("Nome inválido")
    if not validar_endereco(endereco):
        raise ValueError("Endereço inválido")
    if not validar_contato(contato):
        raise ValueError("Contato inválido. Use formato com DDD e número.")
    if not validar_cpf(cpf):
        raise ValueError("CPF inválido")

    cliente = Cliente(nome=nome, endereco=endereco, contato=contato, cpf=cpf)
    cliente.salvar()
    return cliente.to_dict()

def atualizar_cliente(id_cliente: int, data: dict):
    cliente = Cliente.consultar(id_cliente)
    if not cliente:
        return None

    nome = data.get("nome", cliente.nome)
    endereco = data.get("endereco", cliente.endereco)
    contato = data.get("contato", cliente.contato)
    cpf = data.get("cpf", cliente.cpf)

    # Validações
    if not validar_nome(nome):
        raise ValueError("Nome inválido")
    if not validar_endereco(endereco):
        raise ValueError("Endereço inválido")
    if not validar_contato(contato):
        raise ValueError("Contato inválido. Use formato com DDD e número.")
    if not validar_cpf(cpf):
        raise ValueError("CPF inválido")

    cliente.nome = nome
    cliente.endereco = endereco
    cliente.contato = contato
    cliente.cpf = cpf
    cliente.salvar()
    return cliente.to_dict()

def deletar_cliente(id_cliente: int):
    cliente = Cliente.consultar(id_cliente)
    if not cliente:
        return None
    Cliente.excluir(id_cliente)
    return {"mensagem": "Cliente excluído com sucesso"}