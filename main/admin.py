from django.contrib import admin
from .models import Schema, Column


class ColumnInline(admin.TabularInline):
    model = Column
    extra = 1


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    inlines = [ColumnInline]
    list_display = ('name', 'owner', 'created_time')
    search_fields = ('name', 'owner__username')
