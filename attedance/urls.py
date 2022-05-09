from django.urls import path

from . import views
urlpatterns = [
    path("attedance", views.attedance, name="attedance")
   
]
