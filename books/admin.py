from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Book,Review

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('published_date','title')  # Change to tuple with a trailing comma
    search_fields = ('author',)  # Change to tuple with a trailing comma
    pass


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('review_date','reviewer_name')  # Change to tuple with a trailing comma
    search_fields = ('reviewer_name',)  # Change to tuple with a trailing comma
    pass