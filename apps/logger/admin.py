from django.contrib import admin
from .models import Log

class ErrorLogListFilter(admin.SimpleListFilter):
    title = 'response_status'
    parameter_name = 'response_status'
    
    def lookups(self, request, model_admin):
        return (('error', 'error'), ('ok', 'ok'))
        
    def queryset(self, request, queryset):
        if self.value() == 'error':
            return queryset.exclude(response_status__gte=200,
                                    response_status__lt=400)
        elif self.value() == 'ok':
            return queryset.filter(response_status__gte=200,
                                   response_status__lt=400) 

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    ordering = ('-timestamp',)
    list_filter = (ErrorLogListFilter,)