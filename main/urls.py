from django.urls import path

from main.apps import MainConfig
from main.views import index, contacts, StudentDetailView, StudentListView, StudentCreateView

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('students/', StudentListView.as_view(), name='students_list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_item'),
    path('students/create/', StudentCreateView.as_view(), name='students_create'),
]
