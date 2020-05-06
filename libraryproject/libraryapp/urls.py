from django.urls import path, include
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('librarians/', list_librarians, name='librarians'),
    path('libraries/', library_list, name='libraries'),
    path('logout/', logout_user, name='logout'),
    path('book/form', book_form, name='book_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('library/form', library_form, name='library _form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
    path('libraries/<int:library_id>/', library_details, name='library'),

]