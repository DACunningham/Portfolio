from typing import Dict
from django.views.generic import ListView
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# from rest_framework import viewsets, permissions, status
# from rest_framework.exceptions import ParseError
# from rest_framework.parsers import FileUploadParser
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import UserSerializer, GroupSerializer
from .models import Transaction
from .forms import UploadFile
import csv
from datetime import datetime
from decimal import Decimal

# Create your views here.


def upload_file(request):
    if request.method == "POST":
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES["file"]
            arr = []
            for line in f:
                parsed_line = line.decode()
                arr.append(parsed_line)

            test = csv.DictReader(arr)
            # for line in test:
            #     print(line)

            # del arr[0]

            for line in test:
                transaction = _process_data_line(line)
                transaction.save()
            # print(arr)
            return HttpResponseRedirect("/stocks")
    else:
        form = UploadFile()
    return render(request, "stocks/upload.html", {"form": form})


def _process_data_line(data_line: Dict) -> Transaction:
    """
    docstring
    """
    # d = datetime.strftime(data_line["Time"], "%d/%m/%Y %H:%M:%S")
    # a = datetime.strptime(data_line["Time"], "%d/%m/%Y %H:%M")
    transaction = Transaction()
    transaction.transaction_id = data_line["ID"]
    transaction.action = data_line["Action"]
    transaction.time = datetime.strptime(data_line["Time"], "%Y-%m-%d %H:%M:%S")
    transaction.isin = data_line["ISIN"]
    transaction.name = data_line["Name"]
    transaction.share_quantity = data_line["No. of shares"] if data_line["No. of shares"] else None
    transaction.price_per_share = data_line["Price / share"] if data_line["Price / share"] else None
    transaction.currency = data_line["Currency (Price / share)"]
    transaction.exchange_rate = (
        _not_available_check(data_line["Exchange rate"]) if data_line["Exchange rate"] else None
    )
    transaction.result = data_line["Result (GBP)"] if data_line["Result (GBP)"] else None
    transaction.total = data_line["Total (GBP)"] if data_line["Total (GBP)"] else None
    transaction.witholding_tax = (
        data_line["Withholding tax"] if data_line["Withholding tax"] else None
    )
    transaction.witholding_tax_currency = data_line["Currency (Withholding tax)"]
    transaction.charge_amount = (
        data_line["Charge amount (GBP)"] if data_line["Charge amount (GBP)"] else None
    )
    transaction.stamp_duty = (
        data_line["Stamp duty (GBP)"] if data_line["Stamp duty (GBP)"] else None
    )
    transaction.stamp_duty_reserve_tax = (
        data_line["Stamp duty reserve tax (GBP)"]
        if data_line["Stamp duty reserve tax (GBP)"]
        else None
    )
    transaction.finra_fee = data_line["Finra fee (GBP)"] if data_line["Finra fee (GBP)"] else None
    transaction.notes = data_line["Notes"]

    return transaction


def _not_available_check(item_to_test):
    if isinstance(item_to_test, Decimal):
        return item_to_test
    return None


class TransactionList(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "stocks/index.html"


# class UserViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """

#     queryset = User.objects.all().order_by("-date_joined")
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """

#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class TransactionViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.AllowAny]


# class MyFileView(LoginRequiredMixin, APIView):
#     # MultiPartParser AND FormParser
#     # https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
#     # "You will typically want to use both FormParser and MultiPartParser
#     # together in order to fully support HTML form data."
#     parser_classes = [FileUploadParser]

#     def post(self, request, *args, **kwargs):
#         if "file" not in request.data:
#             raise ParseError("Not file uploaded")

#         f = request.data["file"]
#         arr = []
#         for line in f:
#             parsed_line = line.decode()
#             arr.append((parsed_line))
#         # with open(f, newline="") as file:
#         #     reader = csv.DictReader(file)
#         #     # for line in reader:
#         #     #     print(line)
#         #     # print(reader[1])

#         # mymodel.my_file_field.save(f.name, f, save=True)
#         return Response(status=status.HTTP_200_OK)

#         # file_serializer = UserDataUploadSerializer(data=request.data)
#         # if file_serializer.is_valid():
#         #     file_serializer.save()
#         #     return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         # else:
#         #     return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
