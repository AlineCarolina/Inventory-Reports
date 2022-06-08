from inventory_report.inventory.product import Product


def test_cria_produto():
    produto_criado = Product(
        4,
        'notebook',
        'Apple',
        '08/06/2022',
        '08/06/2032',
        '728465287479',
        'manter seguro',
    )
    assert produto_criado.id == 4
    assert produto_criado.nome_do_produto == 'notebook'
    assert produto_criado.nome_da_empresa == 'Apple'
    assert produto_criado.data_de_fabricacao == '08/06/2022'
    assert produto_criado.data_de_validade == '08/06/2032'
    assert produto_criado.instrucoes_de_armazenamento == 'manter seguro'
