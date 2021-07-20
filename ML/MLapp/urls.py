from django.urls import path
from . import views

#MLapps URLS 

urlpatterns = [
    path('', views.main, name='main-page'),
    path('prediction/', views.prediction, name='prediction-page'),
    
]