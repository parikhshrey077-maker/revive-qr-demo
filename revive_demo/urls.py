from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from lights import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda r: HttpResponse("🌟 ReVive QR Demo LIVE! Scan QR → LightPassport instant! ☀️")), 
    path('light/<str:light_id>/light_passport.html', views.light_passport, name='light_passport'),
    path('qr/<str:light_id>/', views.generate_qr, name='generate_qr'),
]
