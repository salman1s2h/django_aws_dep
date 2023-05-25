from django.urls import path
from app import views

urlpatterns = [
    # path('', views.hello),
    # path('job/<int:id>', views.job_details)
    path('', views.job_list, name='jobs_home'),
    path('hello/', views.hello, name='hello'),
    path('job/<slug:slug>', views.job_detail, name='jobs_detail'),
]