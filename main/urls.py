from django.urls import path

from main.apps import MainConfig
from main.views import index, contacts, StudentDetailView, StudentListView, StudentCreateView, StudentUpdateView, \
    StudentDeleteView, toggle_activity

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('students/', StudentListView.as_view(), name='students_list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_item'),
    path('students/create/', StudentCreateView.as_view(), name='students_create'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='students_update'),
    path('students/delete/<int:pk>/', StudentDeleteView.as_view(), name='students_delete'),
    path('students/toggle/<int:pk>/', toggle_activity, name='toggle_activity'),
]
