from django.contrib import admin
from catalog.models import Author, Book, BookInstance, Genre

# Register your models here.
app_models = [Author, Book, BookInstance, Genre]

admin.site.register(app_models) 