from inventory_report.inventory.product import Product


def test_relatorio_produto():
    new_product = Product(
        1, "mouse", "Razer", "28/08/2022", "30/12/2070", "xp-000015", "query"
    )
    to_compare = (
        "O produto mouse fabricado em 28/08/2022 por Razer "
        "com validade até 30/12/2070 precisa ser armazenado query."
    )

    assert str(new_product) == to_compare
