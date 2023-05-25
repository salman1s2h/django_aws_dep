from django.urls import path
from . import views


urlpatterns = [
    path('subscribe/', views.subscribes, name='subscribe'),
    path('thank_you/', views.thank_you, name='thank_you'),

]