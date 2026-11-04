from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('histoire/', views.histoire_view, name='histoire'),
    path('actualites/', views.actualites, name='actualites'),
    path('contact/', views.contact, name='contact'),
]
