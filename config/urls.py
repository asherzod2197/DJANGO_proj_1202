from django.contrib import admin
from django.urls import path
from blog.views import posts_list, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts_list, name='index'),
    path('post_detail/', post_detail, name='post_detail'),
]
