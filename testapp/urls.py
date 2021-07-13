from django.urls import path
from .import views
urlpatterns = [
    path('hello/',views.greeting),
    path('about/',views.about),
    path('contect/',views.contect),
]
