from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('add_show', views.addShow),
    path('shows/<int:show_id>', views.showDetails),
    path('shows/<int:show_id>/edit', views.editShow),
    path('shows/<int:show_id>/delete', views.deleteShow),
]