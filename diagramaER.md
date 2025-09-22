```mermaid
erDiagram
    PESSOA {
        int id PK
        string nome
        date data_nasc
    }

    CONTATO {
        int id PK
        string telefone
        string email
        string whatsapp
    }

    ENDERECO {
        int id PK
        string rua
        string numero
        string bairro
        string cidade
        string estado
    }

    CLIENTE {
        int id_cliente PK, FK
    }

    FUNCIONARIO {
        int id_funcionario PK, FK
        float salario
        string carteira_de_trabalho
        string horario_expediente
    }

    CARGO {
        int id PK
        string nome
        float salario_base
    }

    ORDEM_SERVICO {
        int id PK
        string nome_cliente FK
        string nome_funcionario FK
        date data_emissao
        float valor_total
        string situacao
        string descricao
    }

    ITEM_OS {
        int id PK
        string descricao
        int equipamento_id FK
    }

    EQUIPAMENTO {
        int id PK
        string tipo
        string marca
        string modelo
        int quantidade
    }

    VISITA_TECNICA {
        int id PK
        int ordem_id FK
        int funcionario_id FK
        string horario
    }

    CONTA_RECEBER {
        int id PK
        int ordem_id FK
        float valor
        date data_pagamento
        float acrescimo
    }

    PAGAR_CONTA {
        int id PK
        int conta_id FK
        date data_vencimento
        float valor
        string descricao
    }

    %% RELACIONAMENTOS
    PESSOA ||--|| CONTATO : possui
    PESSOA ||--|| ENDERECO : reside
    PESSOA ||--|| CLIENTE : especializa
    PESSOA ||--|| FUNCIONARIO : especializa
    FUNCIONARIO }o--|| CARGO : ocupa
    ORDEM_SERVICO }o--|| CLIENTE : pertence
    ORDEM_SERVICO }o--|| FUNCIONARIO : atendida_por
    ORDEM_SERVICO ||--o{ ITEM_OS : contem
    ITEM_OS }o--|| EQUIPAMENTO : utiliza
    VISITA_TECNICA }o--|| ORDEM_SERVICO : refere
    VISITA_TECNICA }o--|| FUNCIONARIO : executada_por
    CONTA_RECEBER ||--|| ORDEM_SERVICO : referente
    PAGAR_CONTA ||--|| CONTA_RECEBER : paga


    EMPREGADO ||--o{ PONTO : registra
    DIA_SEMANA ||--o{ PONTO : ocorre_em
    TURNO ||--o{ PONTO : no_turno

