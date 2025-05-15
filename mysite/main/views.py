from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(response):
    return HttpResponse(" Hello, world !! Welcome to index-01 !! ")

def index2(response):
    return HttpResponse(" Hello, world !! Welcome to index-02 !! ")

