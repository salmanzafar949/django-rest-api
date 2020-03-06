from django.urls import path
from .views import BlogPostRudView, BlogPostApiView, getData

urlpatterns = [
    path('', BlogPostApiView.as_view()),
    path('<int:pk>', BlogPostRudView.as_view()),
    path('data', getData)
]
