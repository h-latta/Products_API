from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:pk>/', views.Product_By_ID.as_view())
]