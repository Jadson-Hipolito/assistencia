import re

# ============================
# 🔹 Validadores para Cliente
# ============================

def validar_nome(nome):
    return bool(nome.strip())

def validar_endereco(endereco):
    return bool(endereco.strip())

def validar_contato(contato):
    # Aceita formatos como (84)99999-9999 ou 84999999999
    return bool(re.match(r"^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$", contato))

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calcular_digito(cpf, peso):
        soma = sum(int(digito) * (peso - i) for i, digito in enumerate(cpf[:peso-1]))
        resto = (soma * 10) % 11
        return 0 if resto == 10 else resto

    digito1 = calcular_digito(cpf, 10)
    digito2 = calcular_digito(cpf, 11)
    return cpf[-2:] == f"{digito1}{digito2}"

# ============================
# 🔹 Validadores para Conta
# ============================

def validar_id_os(id_os):
    return isinstance(id_os, int) and id_os > 0

def validar_valor(valor):
    return isinstance(valor, float) and valor > 0

def validar_id_conta(id_conta):
    return isinstance(id_conta, int) and id_conta > 0

# ============================
# 🔹 Validadores para Funcionário
# ============================

def validar_horario(horario):
    # Exemplo válido: "08:00 - 17:00"
    return bool(re.match(r"^\d{2}:\d{2}\s*-\s*\d{2}:\d{2}$", horario))

def validar_salario(salario):
    return isinstance(salario, float) and salario > 0

def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    def calcular_digito(cnpj, pesos):
        soma = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    digito1 = calcular_digito(cnpj, [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    digito2 = calcular_digito(cnpj, [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    return cnpj[-2:] == digito1 + digito2

def validar_id_funcionario(id_funcionario):
    return isinstance(id_funcionario, int) and id_funcionario > 0