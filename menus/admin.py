from django.contrib import admin

from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "menu_name", "parent")
    list_filter = ("menu_name",)
    search_fields = ("title",)


admin.site.register(MenuItem, MenuItemAdmin)
