from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('blog/', views.about, name='blog_about')
]