from . import views
from django.urls import path 

urlpatterns = [
    path('blogcreate/',views.blogcreate),
    path('create/',views.blogView),
    path('blogdetails/<int:id>',views.blogdetails),
    path('bloglist/',views.bloglist),
]