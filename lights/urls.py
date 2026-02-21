from django.urls import path
from . import views

urlpatterns = [
    path(
        'light/<str:light_id>/light_passport.html',
        views.light_passport,
        name='light_passport'
    ),
    path('qr/<str:light_id>/', views.generate_qr, name='generate_qr'),
]
