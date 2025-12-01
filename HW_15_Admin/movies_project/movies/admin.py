from django.contrib import admin
from .models import Movie, Genre, Review


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "rating", "reviews_count")
    list_filter = ("release_date", "rating", "genres")
    search_fields = ("title", "description")
    filter_horizontal = ("genres",)

    def reviews_count(self, obj):
        return obj.reviews.count()
    reviews_count.short_description = "К-сть відгуків"

    # Фільми може змінювати тільки суперкористувач
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("movie", "user_name", "short_text", "created_at")
    list_filter = ("created_at", "movie", "user_name")
    search_fields = ("user_name", "text", "movie__title")
    ordering = ("-created_at",)

    def short_text(self, obj):
        return obj.text[:40] + ("..." if len(obj.text) > 40 else "")
    short_text.short_description = "Текст"

    # Доступ модераторів
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return request.user.has_perm("movies.can_moderate_reviews")

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return request.user.has_perm("movies.can_moderate_reviews")

    def has_add_permission(self, request):
        return False
