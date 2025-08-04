
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('new/', views.create_student, name='create_student'), # <-- Check this line
    path('<int:pk>/edit/', views.update_student, name='update_student'),
    path('<int:pk>/delete/', views.delete_student, name='delete_student'),
]