from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Using function base view
def taskList(request):
    return HttpResponse('To-Do Lists')

