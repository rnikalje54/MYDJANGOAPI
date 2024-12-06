from django.contrib import admin
from .models import Client
from .models import Project


class ClientAdmin(admin.ModelAdmin):
    list_display= ('client_name','created_at','created_by')
    search_fields = ['client_name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','client','created_at')
    search_fields = ['project_name']


admin.site.register(Client,ClientAdmin)
admin.site.register(Project,ProjectAdmin)