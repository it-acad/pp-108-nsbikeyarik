from django.contrib import admin
from .models import Order
from author.models import Author

class BookAuthorFilter(admin.SimpleListFilter):
    title = 'Author'  # Displayed title in the filter sidebar
    parameter_name = 'author'  # The query parameter for filtering

    def lookups(self, request, model_admin):
        # Retrieve all authors to populate the filter dropdown
        return [(author.id, author.name) for author in Author.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            # Filter orders where the book has the selected author
            return queryset.filter(book__authors__id=self.value())
        return queryset

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_info', 'get_book_info', 'created_at', 'end_at', 'plated_end_at')
    list_filter = (
        'created_at',
        'end_at',
        'book__id',  # Filter by Book ID
        'book__name',  # Filter by Book Title
        BookAuthorFilter,  # Custom filter to filter by author
    )
    search_fields = ('user__id', 'book__id', 'user__username', 'book__name')  # Searching by related fields
    fieldsets = (
        ('Order Information', {'fields': ('user', 'book', 'end_at', 'plated_end_at')}),  # Exclude created_at
    )
    exclude = ('created_at',)  # Ensure created_at is excluded from form
    readonly_fields = ('created_at',)  # Make sure created_at is read-only

    def get_user_info(self, obj):
        return f"{obj.user.username} (ID: {obj.user.id})"
    get_user_info.short_description = 'User'

    def get_book_info(self, obj):
        return f"{obj.book.name} (ID: {obj.book.id})"
    get_book_info.short_description = 'Book'

admin.site.register(Order, OrderAdmin)
