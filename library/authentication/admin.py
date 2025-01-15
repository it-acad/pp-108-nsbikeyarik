from django.contrib import admin
from .models import CustomUser

# Custom User Admin
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'role', 'is_active', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('role', 'is_active')
    readonly_fields = ('created_at', 'updated_at')  # Mark non-editable fields as read-only
    fieldsets = (
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'role')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
