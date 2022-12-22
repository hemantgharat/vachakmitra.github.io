
from django import http
from django.http import HttpResponse
from django.shortcuts import HttpResponse, render
from .models import Story_Details
from .serializers import StorySerializer
from rest_framework.generics import ListAPIView

class StoryList(ListAPIView):
    queryset = Story_Details.objects.all()
    serializer_class = StorySerializer

    # bookDesc= Book_Details.objects.last()
    # print (bookDesc)
    # file = open(str(bookDesc), 'r')
    # for book_input in bookDesc:
    #     print (book_input)


def index(request):
    return render(request,'index.html')