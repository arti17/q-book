from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from .forms import EntryForm


def index(request):
    entries = Entry.objects.filter(status='active').order_by('-create_date')
    return render(request, 'index.html', {'entries': entries})


def create(request):
    if request.method == 'GET':
        form = EntryForm()
        return render(request, 'create.html', {'form': form})

    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            Entry.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})


def update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)

    if request.method == 'GET':
        form = EntryForm(data={
            'author': entry.author,
            'email': entry.email,
            'text': entry.text
        })
        return render(request, 'update.html', context={'form': form, 'entry': entry})

    if request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry.author = form.cleaned_data['author']
            entry.email = form.cleaned_data['email']
            entry.text = form.cleaned_data['text']
            entry.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form, 'entry': entry})


def delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.delete()
    return redirect('index')
