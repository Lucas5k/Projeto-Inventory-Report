from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        1, "mouse", "Razer", "28/08/2022", "30/12/2070", "xp-000015", "query"
    )

    assert new_product.id == 1
    assert new_product.nome_do_produto == "mouse"
    assert new_product.nome_da_empresa == "Razer"
    assert new_product.data_de_fabricacao == "28/08/2022"
    assert new_product.data_de_validade == "30/12/2070"
    assert new_product.numero_de_serie == "xp-000015"
    assert new_product.instrucoes_de_armazenamento == "query"
