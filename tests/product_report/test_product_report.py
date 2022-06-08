from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto_criado = Product(
        5,
        'caixa de som',
        'JBL',
        '07-06-2022',
        '07-06-2032',
        '467236547',
        'em lugar seguro',
    )

    assert repr(produto_criado) == (
        f"O produto {produto_criado.nome_do_produto}"
        f" fabricado em {produto_criado.data_de_fabricacao}"
        f" por {produto_criado.nome_da_empresa} com validade"
        f" até {produto_criado.data_de_validade} "
        f"precisa ser armazenado {produto_criado.instrucoes_de_armazenamento}."
        )
