# Пути
from django.urls import path

# REST FRAMEWORK
from rest_framework.schemas import get_schema_view

from .api import (
    ServiceList,
    ServiceListByID,
    CommentList,
    CommentListByID,
    SwaggerDocumentationTemplateView,
)


# Представления
from .views import (
    ServiceListView,
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    SearchView,
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
    # -----------------------------------------------------
    path('service/', ServiceList.as_view(), name='service'),
    path('service/<int:pk>/', ServiceListByID.as_view(), name='service_id'),
    path('comment/', CommentList.as_view(), name='comment'),
    path('comment/<int:pk>/', CommentListByID.as_view(), name='comment_id'),
    path('openapi/', schema, name='openapi'),
    path('swagger_docs/', SwaggerDocumentationTemplateView.as_view(), name='swagger_ui')
]

