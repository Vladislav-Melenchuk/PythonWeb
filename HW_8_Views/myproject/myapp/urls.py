from django.urls import path
from .views import (
    get_item,
    normalize_user_data,
    detect_device,
    get_data_by_key,
    update_data,
    restricted_area,
)

urlpatterns = [
    path('data/item/<int:item_id>/', get_item),
    path('normalize/', normalize_user_data),
    path('detect/', detect_device),
    path('restricted-area/', restricted_area),
    path('data/<str:key>/', get_data_by_key),
    path('update-data/', update_data),
]
