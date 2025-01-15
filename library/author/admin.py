from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic', 'get_book_titles')  # Custom method to display book titles
    list_filter = ('surname',)
    search_fields = ('name', 'surname', 'patronymic')
    fieldsets = (
        ('Author Information', {'fields': ('name', 'surname', 'patronymic')}),
    )
    readonly_fields = ('get_book_titles',)  # Add the custom method to readonly_fields if needed

    def get_book_titles(self, obj):
        return ", ".join([book.name for book in obj.books.all()])
    get_book_titles.short_description = 'Books'  # Column name in the admin list view

admin.site.register(Author, AuthorAdmin)

# from django.contrib import admin
# from .models import Author
#
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'surname', 'patronymic', 'get_book_titles')  # Add the custom method here
#     list_filter = ('surname',)
#     search_fields = ('name', 'surname', 'patronymic')
#     fieldsets = (
#         ('Author Information', {'fields': ('name', 'surname', 'patronymic')}),
#         ('Books', {'fields': ('books',)}),
#     )
#
#     def get_book_titles(self, obj):
#         return ", ".join([book.name for book in obj.books.all()])
#     get_book_titles.short_description = 'Books'  # This sets the column name in the admin list view
#
# admin.site.register(Author, AuthorAdmin)

