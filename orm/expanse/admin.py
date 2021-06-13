from django.contrib import admin

from .models import SpaceShips, Pilot


class PilotAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "surname")
    search_fields = ("name",)
    list_filter = ("birth_date",)
    empty_value_display = '-пусто-'


class SpaceShipsAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "ship_class", "ship_types",)
    search_fields = ("name",)
    empty_value_display = '-пусто-'
    list_per_page = 30
    ordering = ('name',)
    # readonly_fields = []
    # fieldsets = [
    #     ('Admin', {'fields': []}),
    #     ('More data', {'fields': []}),
    # ]


# admin.site.register(Pilot)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(SpaceShips, SpaceShipsAdmin)