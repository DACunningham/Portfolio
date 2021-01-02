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


class Transaction(models.Model):
    """Model definition for Transaction."""

    order_id = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)
    isin = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=6)
    total_amount = models.DecimalField(max_digits=9, decimal_places=6)
    trading_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    commission = models.DecimalField(max_digits=9, decimal_places=2)
    charges_fees = models.DecimalField(max_digits=9, decimal_places=2)
    order_type = models.CharField(
        max_length=20,
        choices=[
            ("MARKET", "Market"),
        ],
    )
    execution_venue = models.CharField(
        max_length=100,
        choices=[
            ("NASDAQ", "NASDAQ"),
            ("NYSE", "New York Stock Exchange"),
            ("LSE", "London Stock Exchange"),
            ("OTC", "Over the Counter"),
        ],
    )
    exchange_rate = models.DecimalField(max_digits=4, decimal_places=2)
    total_cost = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.CharField(
        max_length=3,
        choices=[
            ("GBP", "Great British Pound"),
            ("USD", "United States Dollar"),
            ("EUR", "Euro"),
        ],
    )

    class Meta:
        """Meta definition for Transaction."""

        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        """Unicode representation of Transaction."""
        return f"{self.order_id} - {self.instrument}"
