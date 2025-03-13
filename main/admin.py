from django.contrib import admin
from .models import CustomUser, Article, Team
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ('Extra Information', {'fields': ('birth_date', 'address', 'image')}),
        ('Status', {'fields': ('is_staff', 'is_active')}),
    )

admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(Article)
admin.site.register(Team)