from django.urls import path

from .views import categoriesEndpointView, categoriesGetEndpointView

urlpatterns = [
    path('categories/', categoriesEndpointView, name='categories'),
    path('categories/<int:pk>', categoriesGetEndpointView, name='getcategories'),
]