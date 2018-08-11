from django.contrib import admin
from .models import ClusterData, ProjectData, ModuleData, ErrorData
# Register your models here.


class ClusterAdmin(admin.ModelAdmin):
    list_display = ('cluster_id','cluster_name','cluster_description')
    list_per_page = 25

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'project_description')
    list_per_page = 25

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('module_id','module_name','module_description')
    list_per_page = 25

class ErrorAdmin(admin.ModelAdmin):
    list_display = ('error_id', 'error_name', 'error_description','error_mitigation','link_valid','screenshot_link','author','error_validated','error_validator','editors_list')
    list_per_page = 25

admin.site.register(ClusterData, ClusterAdmin)
admin.site.register(ProjectData, ProjectAdmin)
admin.site.register(ModuleData, ModuleAdmin)
admin.site.register(ErrorData, ErrorAdmin)