from fastapi import HTTPException
from assistencia_tecnica.models.equipamento import Equipamento
from assistencia_tecnica.models.cliente import Cliente
import sqlite3


def listar_equipamentos():
    """Retorna todos os equipamentos cadastrados"""
    equipamentos = Equipamento.listar_todos()
    return [e.to_dict() for e in equipamentos]


def obter_equipamento(id_equipamento: int):
    """Retorna um equipamento específico pelo ID"""
    equipamento = Equipamento.consultar(id_equipamento)
    if not equipamento:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")
    return equipamento.to_dict()


def criar_equipamento(data: dict):
    """Cria um novo equipamento"""
    tipo = data.get("tipo")
    marca = data.get("marca")
    modelo = data.get("modelo")
    numero_serie = data.get("numero_serie")
    id_cliente = data.get("id_cliente")

    # Validações simples
    if not tipo or not isinstance(tipo, str):
        raise HTTPException(status_code=400, detail="Tipo de equipamento inválido")
    if not marca or not isinstance(marca, str):
        raise HTTPException(status_code=400, detail="Marca inválida")
    if not modelo or not isinstance(modelo, str):
        raise HTTPException(status_code=400, detail="Modelo inválido")
    if not numero_serie or not isinstance(numero_serie, str):
        raise HTTPException(status_code=400, detail="Número de série inválido")
    if not id_cliente or not isinstance(id_cliente, int):
        raise HTTPException(status_code=400, detail="ID do cliente inválido")

    # Verifica se o cliente existe
    if not Cliente.consultar(id_cliente):
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    try:
        equipamento = Equipamento(
            tipo=tipo,
            marca=marca,
            modelo=modelo,
            numero_serie=numero_serie,
            id_cliente=id_cliente
        )
        equipamento.salvar()
        return equipamento.to_dict()
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Erro de integridade: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")


def atualizar_equipamento(id_equipamento: int, data: dict):
    """Atualiza um equipamento existente"""
    equipamento = Equipamento.consultar(id_equipamento)
    if not equipamento:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")

    tipo = data.get("tipo", equipamento.tipo)
    marca = data.get("marca", equipamento.marca)
    modelo = data.get("modelo", equipamento.modelo)
    numero_serie = data.get("numero_serie", equipamento.numero_serie)
    id_cliente = data.get("id_cliente", equipamento.id_cliente)

    # Validações simples
    if not tipo or not isinstance(tipo, str):
        raise HTTPException(status_code=400, detail="Tipo de equipamento inválido")
    if not marca or not isinstance(marca, str):
        raise HTTPException(status_code=400, detail="Marca inválida")
    if not modelo or not isinstance(modelo, str):
        raise HTTPException(status_code=400, detail="Modelo inválido")
    if not numero_serie or not isinstance(numero_serie, str):
        raise HTTPException(status_code=400, detail="Número de série inválido")
    if not id_cliente or not isinstance(id_cliente, int):
        raise HTTPException(status_code=400, detail="ID do cliente inválido")

    # Verifica se o cliente existe
    if not Cliente.consultar(id_cliente):
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    try:
        equipamento.tipo = tipo
        equipamento.marca = marca
        equipamento.modelo = modelo
        equipamento.numero_serie = numero_serie
        equipamento.id_cliente = id_cliente
        equipamento.salvar()
        return equipamento.to_dict()
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Erro de integridade: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")


def deletar_equipamento(id_equipamento: int):
    equipamento = Equipamento.consultar(id_equipamento)
    if not equipamento:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")

    Equipamento.excluir(id_equipamento)
    return {"mensagem": "Equipamento excluído com sucesso"}