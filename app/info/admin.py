from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'height', 'weight')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'age', 'height', 'weight')
    list_editable = ('age',)
    list_filter = ('age',)


admin.site.register(UserProfile, UserProfileAdmin)
