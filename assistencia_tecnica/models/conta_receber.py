class ContaReceber:
    def __init__(self, id_conta, os, valor, data_vencimento):
        self.id_conta = id_conta
        self.os = os
        self.valor = valor
        self.status = "Pendente"
        self.data_vencimento = data_vencimento
        self.data_pagamento = None

    def pagar(self, data_pagamento):
        self.status = "Pago"
        self.data_pagamento = data_pagamento

