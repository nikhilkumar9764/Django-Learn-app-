from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Youtuber


def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request , id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)

def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        search_token = request.GET['keyword']
        if search_token:
           tubers = Youtuber.objects.filter(description__icontains=search_token)

    data = {
        'tubers' : tubers
    }
    return render(request, 'youtubers/search.html', data)