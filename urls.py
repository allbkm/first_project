from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('current_time/', views.current_time_view, name='current_time'),
    path('workdir/', views.workdir_view, name='workdir'),
]
