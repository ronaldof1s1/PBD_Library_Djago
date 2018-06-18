from django.urls import path

from . import views


app_name = 'PBD_library'
urlpatterns = [
                path('', views.index, name='index'),
                path('books_list', views.books_list, name='books_list'),
                path('book/<int:book_id>', views.book_detail, name='book_detail'),
                path('users_list', views.users_list, name='users_list'),
                path('user/<int:user_id>', views.user_detail, name='user_detail'),

]