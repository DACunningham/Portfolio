"""
Defines all models for the stocks application.
"""
from django.db import models

# Create your models here.
# class Stock(models.Model):
#     """Model definition for Stock."""

#     instrument = models.CharField(max_length=5)
#     full_name = models.CharField(max_length=100)
#     market = models.CharField(
#         max_length=20,
#         choices=[
#             ("NASDAQ", "NASDAQ"),
#             ("NYSE", "New York Stock Exchange"),
#             ("LSE", "London Stock Exchange"),
#         ],
#     )
#     currency = models.CharField(
#         max_length=5,
#         choices=[
#             ("USD", "United States Dollars"),
#             ("GBP", "Great British Pound"),
#         ],
#     )

#     class Meta:
#         """Meta definition for Stock."""

#         verbose_name = "Stock"
#         verbose_name_plural = "Stocks"

#     def __str__(self):
#         """Unicode representation of Stock."""
#         return f"{self.instrument} - {self.full_name}"

ACTIONS = [
    ("DEPOSIT", "Deposit"),
    ("MARKET_BUY", "Market buy"),
    ("DIVIDEND_ORDINARY", "Dividend (Ordinary)"),
    ("STOP_LIMIT_SELL", "Stop Limit Sell"),
    ("STOP_LIMIT_BUY", "Stop Limit Buy"),
]
CURRENCIES = [
    ("GBP", "Great British Pound"),
    ("GBX", "Great British Pound in Pence"),
    ("USD", "United States Dollar"),
    ("EUR", "Euro"),
]


class Transaction(models.Model):
    """Model definition for Transaction."""

    transaction_id = models.CharField(max_length=200, blank=True)
    action = models.CharField(
        max_length=20,
        choices=ACTIONS,
    )
    time = models.DateTimeField()
    isin = models.CharField(max_length=15, blank=True)
    name = models.CharField(max_length=200, blank=True)
    share_quantity = models.DecimalField(max_digits=19, decimal_places=8, null=True)
    price_per_share = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    currency = models.CharField(
        max_length=20,
        choices=CURRENCIES,
        blank=True,
    )
    exchange_rate = models.DecimalField(max_digits=15, decimal_places=8, null=True)
    result = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    total = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    witholding_tax = models.DecimalField(max_digits=15, decimal_places=8, null=True)
    witholding_tax_currency = models.CharField(
        max_length=20,
        choices=CURRENCIES,
        blank=True,
    )
    charge_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    stamp_duty = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    stamp_duty_reserve_tax = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    finra_fee = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    notes = models.CharField(max_length=500, blank=True)

    class Meta:
        """Meta definition for Transaction."""

        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ["time"]

    def __str__(self):
        """Unicode representation of Transaction."""
        return f"{self.pk} - {self.action} - {self.isin}"
