from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("view_books/", views.view_books, name="view_books"),
    path("admin_signup/", views.admin_signup, name="admin_signup"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logout/", views.Logout, name="logout"),
    path("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
]