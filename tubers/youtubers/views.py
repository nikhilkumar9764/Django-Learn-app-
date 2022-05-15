from django.shortcuts import render

# Create your views here.
from .models import Youtuber


def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request , id):
    return render(request, 'youtubers/youtuber_detail.html')

def search(request):
    pass