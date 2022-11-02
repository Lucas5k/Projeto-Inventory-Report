from datetime import date
import statistics


class SimpleReport:
    @staticmethod
    def generate(list_of_report):
        current_year = str(date.today())
        validate_date = []
        for report in list_of_report:
            min_year = [
                product["data_de_fabricacao"] for product in list_of_report
            ]
            old_year = min(min_year)
            if report["data_de_validade"] > current_year:
                validate_date.append(report["data_de_validade"])
            name = [name["nome_da_empresa"] for name in list_of_report]
            return_name = statistics.mode(name)
        result = (
            f"Data de fabricação mais antiga: {old_year}\n"
            f"Data de validade mais próxima: {min(validate_date)}\n"
            f"Empresa com mais produtos: {return_name}"
        )
        return result
