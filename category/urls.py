from django.urls import path

from .views import categoriesEndpointView, categoriesGetEndpointView

urlpatterns = [
    path('categories/', categoriesEndpointView, name='categories'),
    path('categories/<int:category_id>/', categoriesGetEndpointView, name='getcategories'),
]