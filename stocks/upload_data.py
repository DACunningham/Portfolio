"""
Handles data input to the stocks app
"""

from typing import Dict
from .models import Transaction


def process_input(data: Dict):
    data.pop(0)
    for line in data:
        transaction = process_data_line(line)
        transaction.save()


def process_data_line(data_line: Dict) -> Transaction:
    """
    docstring
    """
    transaction = Transaction()
    transaction.transaction_id = data_line["transaction_id"]
    transaction.action = data_line["action"]
    transaction.time = data_line["time"]
    transaction.isin = data_line["isin"]
    transaction.name = data_line["name"]
    transaction.share_quantity = data_line["share_quantity"]
    transaction.price_per_share = data_line["price_per_share"]
    transaction.currency = data_line["currency"]
    transaction.exchange_rate = data_line["exchange_rate"]
    transaction.result = data_line["result"]
    transaction.total = data_line["total"]
    transaction.witholding_tax = data_line["witholding_tax"]
    transaction.witholding_tax_currency = data_line["witholding_tax_currency"]
    transaction.charge_amount = data_line["charge_amount"]
    transaction.stamp_duty = data_line["stamp_duty"]
    transaction.stamp_duty_reserve_tax = data_line["stamp_duty_reserve_tax"]
    transaction.finra_fee = data_line["finra_fee"]
    transaction.notes = data_line["notes"]

    return transaction
