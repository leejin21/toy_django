from django.urls import path

from .views import list_posts

urlpatterns = [
    path('list/', list_posts)
]
