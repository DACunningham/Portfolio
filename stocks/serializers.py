from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Transaction, CURRENCIES, ACTIONS


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class TransactionSerializer(serializers.Serializer):
    transaction_id = serializers.CharField(max_length=200, allow_blank=True)
    action = serializers.ChoiceField(choices=ACTIONS)
    time = serializers.DateTimeField()
    isin = serializers.CharField(max_length=15, allow_blank=True)
    name = serializers.CharField(max_length=200, allow_blank=True)
    share_quantity = serializers.DecimalField(max_digits=19, decimal_places=8, allow_null=True)
    price_per_share = serializers.DecimalField(max_digits=9, decimal_places=2, allow_null=True)
    currency = serializers.ChoiceField(choices=CURRENCIES)
    exchange_rate = serializers.DecimalField(max_digits=15, decimal_places=8, allow_null=True)
    result = serializers.DecimalField(max_digits=13, decimal_places=2, allow_null=True)
    total = serializers.DecimalField(max_digits=13, decimal_places=2, allow_null=True)
    witholding_tax = serializers.DecimalField(max_digits=15, decimal_places=8, allow_null=True)
    witholding_tax_currency = serializers.ChoiceField(choices=CURRENCIES)
    charge_amount = serializers.DecimalField(max_digits=13, decimal_places=2, allow_null=True)
    stamp_duty = serializers.DecimalField(max_digits=9, decimal_places=2, allow_null=True)
    stamp_duty_reserve_tax = serializers.DecimalField(
        max_digits=9, decimal_places=2, allow_null=True
    )
    finra_fee = serializers.DecimalField(max_digits=9, decimal_places=2, allow_null=True)
    notes = serializers.CharField(max_length=500, allow_blank=True)
