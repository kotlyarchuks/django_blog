from django.urls import path
from . import views
from .views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_home'),
    path('blog/', views.about, name='blog_about')
]
