from django.shortcuts import render
from .models import Entry


def index(request):
    entries = Entry.objects.filter(status='active').order_by('-create_date')
    return render(request, 'index.html', {'entries': entries})
