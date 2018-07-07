from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/edit/', views.edit, name='edit'),
    path('new', views.new, name='new'),
]
