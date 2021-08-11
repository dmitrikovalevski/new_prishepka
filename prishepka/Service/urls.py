# Пути
from django.urls import path

# Представления
from .views import (
    ServiceListView,
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    SearchView,

)

urlpatterns = [
    path('', ServiceListView.as_view(), name='home'),
    path('detail/<int:pk>/', ServiceDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/update/', ServiceUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/delete/', ServiceDeleteView.as_view(), name='delete'),
    path('add_service/', ServiceCreateView.as_view(), name='add_service'),
    path('search_result/', SearchView.as_view(), name='search'),

]