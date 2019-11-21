from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add_notes/', views.add_notes, name='add_notes'),
    path('delete_notes/<int:id>/',views.delete_notes,name='delete_notes'),
    path('edit_notes/<int:id>/',views.edit_notes,name='edit_notes'),
]
    