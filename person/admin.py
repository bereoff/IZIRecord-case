from django.contrib import admin

from person.models import Person, Student


class PersonAdmin(admin.ModelAdmin):
    list_filter = ["id", "first_name", "last_name"]
    search_fields = ["id", "first_name", "last_name"]
    ordering = ["first_name"]


class StudentAdmin(admin.ModelAdmin):
    list_filter = ["id", "first_name", "last_name", "grade", "school"]
    search_fields = ["id", "first_name", "last_name", "grade", "school"]
    ordering = ["first_name"]


admin.site.register(Person, PersonAdmin)
admin.site.register(Student, StudentAdmin)
