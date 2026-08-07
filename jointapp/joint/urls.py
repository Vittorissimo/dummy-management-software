from django.urls import path
from . import views

urlpatterns = [
    path('', views.joint, name="list_joint"),
    path("change/<int:id>/", views.change_joint, name="change_joint")
]