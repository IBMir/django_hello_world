from django.shortcuts import render
from h_w.models import Worker

def index_page(request):
    return render(request, 'index.html')