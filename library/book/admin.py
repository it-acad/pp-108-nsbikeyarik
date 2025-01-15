from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count', 'get_author_names')
    list_filter = ('count',)
    search_fields = ('name', 'description')
    fieldsets = (
        ('Basic Information', {'fields': ('name', 'description', 'count')}),
        ('Authors', {'fields': ('authors',)}),
    )

    def get_author_names(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    get_author_names.short_description = 'Authors'

admin.site.register(Book, BookAdmin)

