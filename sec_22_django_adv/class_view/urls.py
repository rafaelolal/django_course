from django import urls
from django.urls import path
from class_view import views

# this app name is also used in template tagging
app_name = 'class_view'

urlpatterns = [
    # name goes into template tagging
    # template tagging is when you do {%url%} in a template
    path('', views.SchoolListView.as_view(), name='list'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('<str:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('update/<str:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<str:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
]
