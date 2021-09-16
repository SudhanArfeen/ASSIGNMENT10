from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('list/',views.List),
    path('login/',views.login),
    path('signup/',views.signup),
    path('contactus/',views.contactUs),
    path('contactsubmit/',views.contactSubmit),
    path('checkout/',views.checkout),
    path('submitcheckout/',views.submitcheckout),
]
