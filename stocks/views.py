from django.views.generic import ListView
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer
from .models import Transaction
from .forms import UploadFile

# Create your views here.


def upload_file(request):
    if request.method == "POST":
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES["file"]
            arr = []
            for line in f:
                parsed_line = line.decode()
                arr.append((parsed_line))
            del arr[0]
            print(arr)
            return HttpResponseRedirect("/stocks")
    else:
        form = UploadFile()
    return render(request, "stocks/upload.html", {"form": form})


class TransactionList(ListView):
    model = Transaction
    template_name = "stocks/index.html"


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


class MyFileView(APIView):
    # MultiPartParser AND FormParser
    # https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
    # "You will typically want to use both FormParser and MultiPartParser
    # together in order to fully support HTML form data."
    parser_classes = [FileUploadParser]

    def post(self, request, *args, **kwargs):
        if "file" not in request.data:
            raise ParseError("Not file uploaded")

        f = request.data["file"]
        arr = []
        for line in f:
            parsed_line = line.decode()
            arr.append((parsed_line))
        # with open(f, newline="") as file:
        #     reader = csv.DictReader(file)
        #     # for line in reader:
        #     #     print(line)
        #     # print(reader[1])

        # mymodel.my_file_field.save(f.name, f, save=True)
        return Response(status=status.HTTP_200_OK)

        # file_serializer = UserDataUploadSerializer(data=request.data)
        # if file_serializer.is_valid():
        #     file_serializer.save()
        #     return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
