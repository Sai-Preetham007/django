from django.urls import path
from developer_app import views

urlpatterns = [
    path("", views.index)
]