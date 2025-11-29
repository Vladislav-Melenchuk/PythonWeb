from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

def home(request):
    movies = Movie.objects.all().order_by('-rating', 'release_date')  
    return render(request, 'movies/home.html', {'movies': movies})

def movie_detail(request, pk):  
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

def movie_edit(request, pk):  
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_edit.html', {'form': form})

def movie_delete(request, pk): 
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('home')
