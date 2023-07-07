from django.urls import path

from newapp import views

urlpatterns = [
    path("",views.admin1,name="admin1"),
    path("First",views.First,name="First"),
    path("task_view",views.task_view,name="task_view"),
    path("delete/<int:id>/",views.delete, name="delete"),
    path("dtails",views.dtails,name="dtails"),
    path("detailsview",views.detailsview,name="detailsview"),
    path("TaskUpdate/<int:id>/",views.TaskUpdate,name="TaskUpdate"),
    path("count",views.count,name="count"),

]