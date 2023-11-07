from django.urls import path
from .views import RestaurantListCreateView, RestaurantRetrieveView

urlpatterns = [
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantRetrieveView.as_view(), name='restaurant-retrieve'),
]