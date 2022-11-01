from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list_of_report):
        simple_report = SimpleReport.generate(list_of_report)
        for quantity in list_of_report:
            one_index_of_list = list_of_report[0].get("nome_da_empresa")
            if one_index_of_list == quantity.get("nome_da_empresa"):
                return_names = quantity.get("nome_da_empresa")
                return_quantitys = len(quantity.get("nome_do_produto"))
        result = (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"- {return_names}: {return_quantitys} "
        )
        return result
