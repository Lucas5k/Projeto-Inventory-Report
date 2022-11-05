from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

products = [
  {
    "id": 1,
    "nome_do_produto": "Cafe",
    "nome_da_empresa": "Cafes Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "instrucao"
  }
]


def test_decorar_relatorio():
    returns = ColoredReport(SimpleReport).generate(products)

    old_year = "\033[32mData de fabricação mais antiga:\033[0m"
    old_date = "\033[36m2020-07-04\033[0m"

    validate_date = "\033[32mData de validade mais próxima:\033[0m"
    current_date = "\033[36m2023-02-09\033[0m"

    return_name = "\033[32mEmpresa com mais produtos:\033[0m"
    name = "\033[31mCafes Nature\033[0m"

    to_compare = (
        f"{old_year} {old_date}\n"
        f"{validate_date} {current_date}\n"
        f"{return_name} {name}"
    )

    assert returns == to_compare
