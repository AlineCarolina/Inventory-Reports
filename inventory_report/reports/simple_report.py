from datetime import date
from collections import Counter


class SimpleReport():
    def oldest_manufacture(list):
        for item in list:
            oldest = date.fromisoformat(item["data_de_fabricacao"])
            return oldest

    def validate_closer(list):
        for item in list:
            closer = date.fromisoformat(item["data_de_validade"])
            return closer

    def company_with_more_products(list):
        [(company, _)] = Counter(
            item["nome_da_empresa"] for item in list
            ).most_common(1)
        return company

    def generate(list):
        oldest = SimpleReport.oldest_manufacture(list)
        closer = SimpleReport.validate_closer(list)
        company = SimpleReport.company_with_more_products(list)

        return (
            f"Data de fabricação mais antiga: {oldest}"
            f"Data de validade mais próxima: {closer}"
            f"Empresa com mais produtos: {company}"
        )
