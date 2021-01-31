from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request, 'core/home.html')

def topics(request, board_number):
    data = {'board_number': board_number}
    return render(request, 'core/topics.html', data)
    