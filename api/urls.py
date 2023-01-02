from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create),
    path('get/', get_item),
    path('status/', status),
    path('item/', item),
]
