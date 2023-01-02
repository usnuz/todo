from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('finish/<int:pk>/', finish, name='finish'),
    path('inprog/', inprog, name='inprog'),
    path('deleted/', deleted, name='deleted'),
    path('finished/', finished, name='finished'),
]