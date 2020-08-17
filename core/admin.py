from django.contrib import admin
from core.models import Interaction

# Register your models here.

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ['id', 'input_value', 'output']
    search_fields = ['output', 'input_value']

