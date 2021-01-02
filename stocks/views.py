from django.views.generic import ListView, DetailView
from .models import Transaction

# Create your views here.
class TransactionList(ListView):
    model = Transaction
    template_name = "stocks/index.html"
