from django.urls import path

from .views import categoriesEndpointView, categoriesGetEndpointView

urlpatterns = [
    path('categories/<int:category_id>/', categoriesGetEndpointView,
         name='getcategories'),
    path('categories/', categoriesEndpointView, name='categories'),
]
