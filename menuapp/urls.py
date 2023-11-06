from django.urls import path
from .views import menu_view,contacts_view,person_view

urlpatterns = [
    path('menu/', menu_view, name='menu'),
    path('contacts/', contacts_view, name='contacts'),
    path('person/', person_view, name='person'),
]