from .models import City, People
from django.contrib import admin


@admin.register(People)
class PeopleInAdmin(admin.ModelAdmin):
    list_display = ("fio", "city")
    search_fields = ["fio"]


@admin.register(City)
class CitiesInAdmin(admin.ModelAdmin):
    list_display = ("id", "cityname")
    search_fields = ["id", "cityname"]
