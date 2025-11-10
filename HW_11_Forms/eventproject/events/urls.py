from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('createevent/', views.create_event, name='create_event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]
