from venv import create
from django.urls import path
from .views import BlogCreateViews, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView

app_name = "blog"

urlpatterns = [
    path('',BlogListView.as_view(), name = "home"),
    path('create/',BlogCreateViews.as_view(), name="create"),
    path('<int:pk>/',BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update',BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete',BlogDeleteView.as_view(), name="delete"),
]
 