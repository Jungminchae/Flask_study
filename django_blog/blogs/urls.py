from django.urls import path 
from . import views

app_name = 'blogs'


urlpatterns = [
    path("post/<int:pk>", views.post_detail , name='post_detail')
]