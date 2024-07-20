import json

def criar_json_completo(itens, pagamentos, codigo_empresa, codigo_empresa_financeiro, identificadores, valores, conhecimento_transporte, tipo_frete, endereco, data_emissao, descricao, prazo, tipo_logradouro, uf):
    json_completo = {
        "Itens": itens,
        "Pagamentos": pagamentos,
        "CodigoEmpresa": codigo_empresa,
        "CodigoEmpresaFinanceiro": codigo_empresa_financeiro,
        "IdentificadorBairro": identificadores["bairro"],
        "IdentificadorCidade": identificadores["cidade"],
        "IdentificadorFornecedor": identificadores["fornecedor"],
        "IdentificadorIndexador": identificadores["indexador"],
        "IdentificadorNaturezaLancamento": identificadores["natureza_lancamento"],
        "IdentificadorTransportador": identificadores["transportador"],
        "IdentificadorUsuarioLiberacao": identificadores["usuario_liberacao"],
        "ValorAcrescimo": valores["acrescimo"],
        "ValorDesconto": valores["desconto"],
        "ValorFrete": valores["frete"],
        "ValorSeguro": valores["seguro"],
        "ValorOutrasDespesas": valores["outras_despesas"],
        "ValorACT": valores["act"],
        "ConhecimentoTransporte": conhecimento_transporte,
        "TipoFrete": tipo_frete,
        "CEP": endereco["cep"],
        "Codigo": endereco["codigo"],
        "ComplementoEndereco": endereco["complemento"],
        "DataEmissao": data_emissao["emissao"],
        "DataEmissaoACT": data_emissao["emissao_act"],
        "DataEntrega": data_emissao["entrega"],
        "Descricao": descricao,
        "IdentificadorEntidadeOrigem": identificadores["entidade_origem"],
        "NomeEntidadeOrigem": identificadores["nome_entidade_origem"],
        "EntregaParcial": endereco["entrega_parcial"],
        "Logradouro": endereco["logradouro"],
        "NumeroEndereco": endereco["numero"],
        "NumeroOrcamento": endereco["orcamento"],
        "Observacao": endereco["observacao"],
        "Prazo": prazo,
        "TipoLogradouro": tipo_logradouro,
        "UF": uf
    }

    return json_completo

# Exemplo de uso
values = {
    "Itens": [
        {
            "IdentificadorPedidoDeCompraItem": "A",
            "TipoCadastro": "A",
            "IdentificadorAplicacao": "00A0000001",
            "IdentificadorProduto": "00A0000001",
            "IdentificadorProdutoLote": "00A0000001",
            "IdentificadorUnidade": "00A0000001",
            "Bonificacao": True,
            "DataEntrega": "2020-06-10T17:53:34.895Z",
            "DataValidade": "2020-06-10T17:53:34.895Z",
            "Observacao": "Item do pedido cadastrado pela api",
            "QuantidadeEmbalagem": 2,
            "QuantidadePedida": 4,
            "ValorUnitario": 25
        }
    ],

    "Pagamentos": [
        {
            "IdentificadorPedidoDeCompraPagamento": "00A0000001",
            "TipoCadastro": "A",
            "IdentificadorContaBancaria": "00A0000001",
            "IdentificadorFormaPagamento": "00A0000001",
            "AliquotaParcela": 10,
            "Antecipado": True,
            "DataReferencia": "2020-06-10T17:53:34.895Z",
            "NumeroDias": 15,
            "Valor": 10
        }
    ],

    "CodigoEmpresa": "01",
    "CodigoEmpresaFinanceiro": "01",
    "IdentificadorBairro": "00A0000001",
    "IdentificadorCidade": "00A0000001",
    "IdentificadorFornecedor": "00A0000001",
    "IdentificadorIndexador": "00A0000001",
    "IdentificadorNaturezaLancamento": "00A0000001",
    "IdentificadorTransportador": "00A0000001",
    "IdentificadorUsuarioLiberacao": "00A0000001",
    "ValorAcrescimo": 1,
    "ValorDesconto": 2,
    "ValorFrete": 3,
    "ValorSeguro": 4,
    "ValorOutrasDespesas": 5,
    "ValorACT": 6,
    "ConhecimentoTransporte": {
        "TransportePagamentos": [
            {
                "IdentificadorContaBancaria": "00A0000001",
                "IdentificadorFormaPagamento": "00A0000001",
                "NumeroTitulo": "123456",
                "DataReferencia": "2020-06-10T17:53:34.896Z",
                "NumeroDias": 15,
                "AliquotaParcela": 10,
                "ValorParcela": 10
            }
        ],
        
        "PrazoTransporte": {
            "Identificador": "00A0000001",
            "IdentificadorFormaPagamentoEntrada": "00A0000001",
            "IdentificadorFormaPagamentoParcelas": "00A0000001"
        }
    },
    "TipoFrete": "D",
    "CEP": "25123123",
    "Codigo": "00001",
    "ComplementoEndereco": "Apto 123",
    "DataEmissao": "2020-06-10T17:53:34.896Z",
    "DataEmissaoACT": "2020-06-10T17:53:34.896Z",
    "DataEntrega": "2020-06-10T17:53:34.896Z",
    "Descricao": "Pedido cadastrado pela BimerAPI",
    "IdentificadorEntidadeOrigem": "00A0000001",
    "NomeEntidadeOrigem": "Entidade",
    "EntregaParcial": True,
    "Logradouro": "Avenida principal",
    "NumeroEndereco": "400",
    "NumeroOrcamento": "123",
    "Observacao": "Cadastrado pela Bimer API",
    "Prazo": {
        "Identificador": "00A0000001",
        "IdentificadorFormaPagamentoEntrada": "00A0000001",
        "IdentificadorFormaPagamentoParcelas": "00A0000001"
    },
    "TipoLogradouro": "A",
    "UF": "RJ"
}

identificadores = {
    "bairro": "00A0000001",
    "cidade": "00A0000001",
    "fornecedor": "00A0000001",
    "indexador": "00A0000001",
    "natureza_lancamento": "00A0000001",
    "transportador": "00A0000001",
    "usuario_liberacao": "00A0000001",
    "entidade_origem": "00A0000001",
    "nome_entidade_origem": "Entidade"
}

valores = {
    "acrescimo": 1,
    "desconto": 2,
    "frete": 3,
    "seguro": 4,
    "outras_despesas": 5,
    "act": 6
}

conhecimento_transporte = {
    "TransportePagamentos": [
        {
            "IdentificadorContaBancaria": "00A0000001",
            "IdentificadorFormaPagamento": "00A0000001",
            "NumeroTitulo": "123456",
            "DataReferencia": "2020-06-10T17:53:34.896Z",
            "NumeroDias": 15,
            "AliquotaParcela": 10,
            "ValorParcela": 10
        }
    ],
    "PrazoTransporte": {
        "Identificador": "00A0000001",
        "IdentificadorFormaPagamentoEntrada": "00A0000001",
        "IdentificadorFormaPagamentoParcelas": "00A0000001"
    }
}

endereco = {
    "cep": "25123123",
    "codigo": "00001",
    "complemento": "Apto 123",
    "entrega_parcial": True,
    "logradouro": "Avenida principal",
    "numero": "400",
    "orcamento": "123",
    "observacao": "Cadastrado pela Bimer API"
}

data_emissao = {
    "emissao": "2020-06-10T17:53:34.896Z",
    "emissao_act": "2020-06-10T17:53:34.896Z",
    "entrega": "2020-06-10T17:53:34.896Z"
}

prazo = {
    "Identificador": "00A0000001",
    "IdentificadorFormaPagamentoEntrada": "00A0000001",
    "IdentificadorFormaPagamentoParcelas": "00A0000001"
}

json_completo = criar_json_completo(
    values["Itens"],
    values["Pagamentos"],
    values["CodigoEmpresa"],
    values["CodigoEmpresaFinanceiro"],
    identificadores,
    valores,
    conhecimento_transporte,
    values["TipoFrete"],
    endereco,
    data_emissao,
    values["Descricao"],
    prazo,
    values["TipoLogradouro"],
    values["UF"]
)

print(json.dumps(json_completo, indent=2))
