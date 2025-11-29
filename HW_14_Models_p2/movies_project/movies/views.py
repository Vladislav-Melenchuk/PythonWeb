from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from .forms import MovieForm, ReviewForm

def home(request):
    movies = Movie.objects.all().order_by('-rating', 'release_date')  
    return render(request, 'movies/home.html', {'movies': movies})

def movie_detail(request, pk):  
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()
    review_count = reviews.count()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = ReviewForm()

    return render(request, 'movies/movie_detail.html', {'movie': movie, 'reviews': reviews, 'form': form, 'review_count': review_count})

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

def delete_review(request, pk):  
    review = get_object_or_404(Review, pk=pk)
    movie_pk = review.movie.pk
    review.delete()
    return redirect('movie_detail', pk=movie_pk)