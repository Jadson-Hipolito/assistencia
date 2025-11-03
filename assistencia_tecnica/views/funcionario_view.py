from fastapi import HTTPException
from assistencia_tecnica.models.funcionario import Funcionario
from assistencia_tecnica.validadores import (
    validar_nome, validar_endereco, validar_contato,
    validar_horario, validar_salario, validar_cnpj
)

def listar_funcionarios():
    return [f.to_dict() for f in Funcionario.listar_todos()]

def obter_funcionario(id_funcionario: int):
    funcionario = Funcionario.consultar(id_funcionario)
    return funcionario.to_dict() if funcionario else None

def criar_funcionario(data: dict):
    nome = data.get("nome")
    endereco = data.get("endereco")
    contato = data.get("contato")
    horario = data.get("horario")

    # Tratamento robusto do salário
    salario_raw = data.get("salario", 0)
    try:
        if isinstance(salario_raw, str):
            salario_raw = salario_raw.replace(",", ".")
        salario = float(salario_raw)
    except (TypeError, ValueError):
        raise HTTPException(status_code=400, detail="Salário inválido")

    cnpj = data.get("cnpj")
    ativo = data.get("ativo", True)

    # Validações
    if not validar_nome(nome):
        raise HTTPException(status_code=400, detail="Nome inválido")
    if not validar_endereco(endereco):
        raise HTTPException(status_code=400, detail="Endereço inválido")
    if not validar_contato(contato):
        raise HTTPException(status_code=400, detail="Contato inválido")
    if not validar_horario(horario):
        raise HTTPException(status_code=400, detail="Horário inválido. Use formato HH:MM - HH:MM")
    if not validar_salario(salario):
        raise HTTPException(status_code=400, detail="Salário inválido")
    if not validar_cnpj(cnpj):
        raise HTTPException(status_code=400, detail="CNPJ inválido")

    funcionario = Funcionario(
        nome=nome,
        endereco=endereco,
        contato=contato,
        horario=horario,
        salario=salario,
        cnpj=cnpj,
        ativo=ativo
    )
    funcionario.salvar()
    return funcionario.to_dict()

def atualizar_funcionario(id_funcionario: int, data: dict):
    funcionario = Funcionario.consultar(id_funcionario)
    if not funcionario:
        return None

    nome = data.get("nome", funcionario.nome)
    endereco = data.get("endereco", funcionario.endereco)
    contato = data.get("contato", funcionario.contato)
    horario = data.get("horario", funcionario.horario)

    # Tratamento robusto do salário
    salario_raw = data.get("salario", funcionario.salario)
    try:
        if isinstance(salario_raw, str):
            salario_raw = salario_raw.replace(",", ".")
        salario = float(salario_raw)
    except (TypeError, ValueError):
        raise HTTPException(status_code=400, detail="Salário inválido")

    cnpj = data.get("cnpj", funcionario.cnpj)
    ativo = data.get("ativo", funcionario.ativo)

    # Validações
    if not validar_nome(nome):
        raise HTTPException(status_code=400, detail="Nome inválido")
    if not validar_endereco(endereco):
        raise HTTPException(status_code=400, detail="Endereço inválido")
    if not validar_contato(contato):
        raise HTTPException(status_code=400, detail="Contato inválido")
    if not validar_horario(horario):
        raise HTTPException(status_code=400, detail="Horário inválido. Use formato HH:MM - HH:MM")
    if not validar_salario(salario):
        raise HTTPException(status_code=400, detail="Salário inválido")
    if not validar_cnpj(cnpj):
        raise HTTPException(status_code=400, detail="CNPJ inválido")

    funcionario.nome = nome
    funcionario.endereco = endereco
    funcionario.contato = contato
    funcionario.horario = horario
    funcionario.salario = salario
    funcionario.cnpj = cnpj
    funcionario.ativo = ativo
    funcionario.salvar()
    return funcionario.to_dict()

def deletar_funcionario(id_funcionario: int):
    funcionario = Funcionario.consultar(id_funcionario)
    if not funcionario:
        return None
    Funcionario.excluir(id_funcionario)
    return {"mensagem": "Funcionário excluído com sucesso"}