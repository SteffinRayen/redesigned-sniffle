from django.db import models
from django.utils import timezone
# Create your models here.


class ClusterData(models.Model):
    cluster_id = models.CharField(max_length=3,unique=True,default="C1")
    cluster_name = models.CharField(max_length = 1000)
    cluster_description = models.CharField(max_length = 1000)
    def __str__(self):
        return "%s" % (self.cluster_name)
    class Meta:
        ordering = ('cluster_id',)
        verbose_name = "Cluster Data"
        verbose_name_plural = "Cluster Data"

class ProjectData(models.Model):
    cluster_id = models.ForeignKey(ClusterData, to_field='cluster_id', on_delete=models.CASCADE)
    project_id = models.CharField(max_length=7,unique=True,default="C1.P1")
    project_name = models.CharField(max_length = 1000)
    project_description = models.CharField(max_length = 1000)
    def __str__(self):
        return "%s" % (self.project_name)
    class Meta:
        ordering = ('project_id',)
        verbose_name = "Project Data"
        verbose_name_plural = "Project Data"

class ModuleData(models.Model):
    project_id = models.ForeignKey(ProjectData, to_field='project_id', on_delete=models.CASCADE)
    module_id = models.CharField(max_length=11,unique=True,default="C1.P1.M1")
    module_name = models.CharField(max_length = 1000)
    module_description = models.CharField(max_length = 1000)
    def __str__(self):
        return "%s" % (self.module_name)
    class Meta:
        ordering = ('module_id',)
        verbose_name = "Module Data"
        verbose_name_plural = "Module Data"

class ErrorData(models.Model):
    module_id = models.ForeignKey(ModuleData, to_field='module_id', on_delete=models.CASCADE)
    error_id = models.CharField(max_length=20,unique=True,default="C1.P1.M1.E1")
    error_name = models.CharField(max_length = 1000)
    error_description = models.CharField(max_length = 1000)
    error_mitigation = models.CharField(max_length = 1000) 
    link_valid = models.BooleanField(default=False)
    screenshot_link = models.CharField(max_length = 1000)
    author = models.CharField(max_length = 1000)
    error_validated = models.BooleanField(default=False)
    error_validator = models.CharField(max_length = 1000)
    editors_list = models.CharField(max_length = 1000)
    def __str__(self):
        return "%s" % (self.error_name)
    class Meta:
        ordering = ('error_id',)
        verbose_name = "Error Data"
        verbose_name_plural = "Error Data"

