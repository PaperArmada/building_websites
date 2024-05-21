from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.viewStudentList, name='viewStudentList'),
    path(r'<int:student_id>/', views.viewStudentDetails, name='viewStudentDetails'),
]