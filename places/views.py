from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import PlaceForm
import random

def home(request):
    return render(request, 'places/home.html')

def place_list(request):
    places = Place.objects.all()
    return render(request, 'places/place_list.html', {'places': places})

def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('places:place_list')
    else:
        form = PlaceForm()
    return render(request, 'places/add_place.html', {'form': form})

def random_place(request):
    places = Place.objects.all()
    if places:
        weights = [place.rating for place in places]
        chosen = random.choices(places, weights=weights, k=1)[0]
        return render(request, 'places/random_place.html', {'place': chosen})
    return redirect('places:home')

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'places/place_detail.html', {'place': place})