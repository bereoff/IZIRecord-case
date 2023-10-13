from django.contrib import admin

from schools.models import School


class SchoolAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "maximum_capacity"]
    list_filter = ["id", "name", "maximum_capacity"]
    search_fields = ["id", "name", "maximum_capacity"]
    ordering = ["name"]


admin.site.register(School, SchoolAdmin)
