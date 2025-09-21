
# Documento Lista de User Stories

Documento construído a partido do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no
link: https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 22/09/2020 | 0.0.1   | Template e descrição do documento  | Jadson |
| 23/09/2020 | 0.0.1   | Detalhamento do User Story US01    | Taciano |
| ...        | ...     | ...                                | ...     |
| 12/07/2020 | 1.0.0   | Documento completo com o detalhamento de todos os User Stories | Taciano     |
| 30/04/2022 | 1.6.0   | Adição das informações da equipe: Analista, Desenvolvedor, Revisor e Testador. | Taciano |



### User Story US01 - Manter Cliente

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir o cadastro detalhado de clientes, incluindo informações como nome, endereço, contato, histórico de serviços, CPF, entre outros. Alem disso sistema deve permitir a alteração de qualquer dado contido no cadastro, a consulta e a exclusão do cliente.
|
| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Cadastrar Cliente |
| RF02          | Alterar Cliente |
| RF03          | Consultar Cliente |
| RF04          | Excluir Cliente |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 8 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     |                                     | 
| **Analista**              | Jadson                              | 
| **Desenvolvedor**         | Jaedson                             | 
| **Revisor**               | Mariana                             | 
| **Testador**              | Jadson                              | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Descrever o teste de aceitação 01 do US01 |
| **TA01.02** | Descrever o teste de aceitação 02 do US01 |
| **TA01.03** | Descrever o teste de aceitação 03 do US01 |
| **TA01.04** | Descrever o teste de aceitação 04 do US01 |


### User Story US02 - Manter Funcionario

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir o cadastro detalhado de funcionários, incluindo informações como nome, endereço, contato, horário de expediente, salário, CNPJ, entre outros. Alem disso o sistema deve permitir a alteração de qualquer dado contido no cadastro do funcionário, a consulta e  desativação do funcionário. 
| 
| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Cadastrar Funcionario |
| RF02          | Alterar Funcionario |
| RF03          | Consultar Funcionario |
| RF04          | Desativar Funcionario |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 8 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     |                                     | 
| **Analista**              | Jaedson                             | 
| **Desenvolvedor**         | Mariana                             | 
| **Revisor**               | Jadson                              | 
| **Testador**              | Jaedson                             | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Descrever o teste de aceitação 01 do US01 |
| **TA01.02** | Descrever o teste de aceitação 02 do US01 |
| **TA01.03** | Descrever o teste de aceitação 03 do US01 |
| **TA01.04** | Descrever o teste de aceitação 04 do US01 |

### User Story US03 - Manter Ordem de Serviço

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir a criação de ordens de serviço para cada solicitação de reparo ou manutenção, com a possibilidade de incluir informações sobre o cliente, descrição do problema e quaisquer detalhes relevantes, a edição dos dados da ordem de serviço, a consulta pela ordem de serviço e qualquer dado contido nele. Alem disso permitir que os funcionários autorizados encerrem ordens de serviço após a conclusão das atividades. E fornecer a capacidade de gerar relatórios diversos, como histórico de serviços realizados, faturamento por período, entre outros. | 
| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Abrir ordem de Serviço |
| RF02          | Editar ordem de serviço |
| RF03          | Consultar ordem de serviço |
| RF04          | Encerrar ordem de serviço |
| RF05          | Emitir Relatório |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 10 h                                | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     |                                     | 
| **Analista**              | Mariana                             | 
| **Desenvolvedor**         | Jadson                              | 
| **Revisor**               | Jaedson                             | 
| **Testador**              | Mariana                             | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Descrever o teste de aceitação 01 do US01 |
| **TA01.02** | Descrever o teste de aceitação 02 do US01 |
| **TA01.03** | Descrever o teste de aceitação 03 do US01 |
| **TA01.04** | Descrever o teste de aceitação 04 do US01 |

### User Story US04 - Manter Equipamento

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir o cadastro detalhado do equipamento, incluindo informações como o id, tipo, marca, modelo e quantidade. O sistema deve permitir a consulta do equipamento através do id do mesmo (include manter Equipamento). O	sistema	deve	permitir	a	exclusão	do	cliente	(include	manter
Equipamento). | 
| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Cadastrar Equipamento |
| RF02          | Consultar Equipamento |
| RF03          | Excluir Equipamento |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 6 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     |                                     | 
| **Analista**              | Jadson                              | 
| **Desenvolvedor**         | Jaedson                             | 
| **Revisor**               | Mariana                             | 
| **Testador**              | Jadson                              | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Descrever o teste de aceitação 01 do US01 |
| **TA01.02** | Descrever o teste de aceitação 02 do US01 |
| **TA01.03** | Descrever o teste de aceitação 03 do US01 |
| **TA01.04** | Descrever o teste de aceitação 04 do US01 |

### User Story US05 - Agendar Visitas Técnicas

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Funcionalidade que permite ao funcionário agendar visitas presenciais para resolver problemas que não podem ser resolvidos remotamente(include manter ordem de serviço). | 
| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Agendar Visitas Técnicas |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 4 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     |                                     | 
| **Analista**              | Jaedson                             | 
| **Desenvolvedor**         | Mariana                             | 
| **Revisor**               | Jadson                              | 
| **Testador**              | Jaedson                              | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Descrever o teste de aceitação 01 do US01 |
| **TA01.02** | Descrever o teste de aceitação 02 do US01 |
| **TA01.03** | Descrever o teste de aceitação 03 do US01 |
| **TA01.04** | Descrever o teste de aceitação 04 do US01 |

### User Story US06 - Registrar Conta Receber

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Ao salvar uma OS é criado um conta receber automaticamente, esse conta receber futuramente pode vir a ser atualizado pelo funcionário da empresa registrando o pagamento do cliente(include manter ordem de serviço). | 
| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Registrar Conta Receber |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 10 h                                | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     |                                     | 
| **Analista**              | Mariana                             | 
| **Desenvolvedor**         | Jadson                              | 
| **Revisor**               | Jaedson                             | 
| **Testador**              | Mariana                             | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Descrever o teste de aceitação 01 do US01 |
| **TA01.02** | Descrever o teste de aceitação 02 do US01 |
| **TA01.03** | Descrever o teste de aceitação 03 do US01 |
| **TA01.04** | Descrever o teste de aceitação 04 do US01 |

### User Story US07 - Pagar Conta

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Ao salvar uma OS é criado um conta receber automaticamente, esse conta receber futuramente pode vir a ser atualizado pelo funcionário da empresa registrando o pagamento do cliente(include manter ordem de serviço). | 
| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Pagar Conta |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 6 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     |                                     | 
| **Analista**              | Jadson                              | 
| **Desenvolvedor**         | Jaedson                             | 
| **Revisor**               | Mariana                             | 
| **Testador**              | Jadson                              | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Descrever o teste de aceitação 01 do US01 |
| **TA01.02** | Descrever o teste de aceitação 02 do US01 |
| **TA01.03** | Descrever o teste de aceitação 03 do US01 |
| **TA01.04** | Descrever o teste de aceitação 04 do US01 |
