from django.urls import path
from .views import detection

urlpatterns = [
    path('detection/',detection,name='detection')
]