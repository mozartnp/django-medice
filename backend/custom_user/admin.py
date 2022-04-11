from django.contrib import admin

from backend.custom_user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'email',
        'user_type',
        'is_active',
        'is_admin',
        'is_staff',
        'is_superuser',
    )
    search_fields = ('email',)
    list_filter = (
        'user_type',
        'is_active',
        'is_admin',
        'is_staff',
        'is_superuser',
    )
