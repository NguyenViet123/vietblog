from django.urls import path, include
from . import views
urlpatterns = [
	path('', views.about),
    path('about', views.about),
    path('blog', views.posts),
    path('blog/<int:id>', views.post)
]
