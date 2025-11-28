from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

def home(request):
    movies = Movie.objects.all()
    return render(request, 'movies/home.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
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
