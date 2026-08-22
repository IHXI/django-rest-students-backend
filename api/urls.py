from django.urls import path

from . import views

urlpatterns = [
    path("students", views.student_list_create, name="student_list_create"),
    path("students/<int:student_id>", views.student_detail, name="student_detail")
]