from django.views import generic
from django.views.generic import View
from django.shortcuts import render


def index(request):

     return render(request, 'index.html')

#def about_pickart(request):
#def how_to_rental(request):
#def example(request):
#def contact_us(request):