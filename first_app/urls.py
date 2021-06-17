from django.conf.urls import  url
from django.urls import path
from . import views

app_name="first_app"

urlpatterns = [

    path("",views.index,name="index"),
    path("add_student/",views.add_student,name="add_student"),
    path("add_subject/",views.add_subject,name="add_subject"),
    path("student_detail/<int:id>",views.student_detail,name="student_detail"),
    path("edit_student/<int:id>",views.edit_info_student,name="edit"),
    path("edit_subject/<int:id>",views.edit_info_subject,name="edit"),
    path("delete_sub/<int:id>",views.delete_subject,name="delete"),
    path("delete_stu/<int:id>",views.delete_student,name="delete"),


]
