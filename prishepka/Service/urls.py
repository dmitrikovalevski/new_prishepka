# Пути
from django.urls import path

# REST FRAMEWORK
from rest_framework.schemas import get_schema_view

# Представления
from .views import (
    ServiceListView,
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    SearchView,
    # REST-FRAMEWORK
    api_comment,
    ServiceApiView,
    SwaggerDocumentationTemplateView,
)

schema = get_schema_view(
    title='Prishepka',
    description='Prishepka API'
)


urlpatterns = [
    path('', ServiceListView.as_view(), name='home'),
    path('detail/<int:pk>/', ServiceDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/update/', ServiceUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/delete/', ServiceDeleteView.as_view(), name='delete'),
    path('add_service/', ServiceCreateView.as_view(), name='add_service'),
    path('search_result/', SearchView.as_view(), name='search'),
    path('api_comment/', api_comment, name='api_comment'),
    path('api_service/', ServiceApiView.as_view()),
    path('openapi/', schema, name='openapi'),
    path('swagger_docs/', SwaggerDocumentationTemplateView.as_view(), name='swagger_ui')
]

