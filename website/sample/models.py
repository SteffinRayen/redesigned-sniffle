from django.db import models
from django.utils import timezone
# Create your models here.


class ClusterData(models.Model):
    cluster_id = models.IntegerField(unique=True, default=timezone.now)
    cluster_description = models.CharField(max_length = 200)
    def __str__(self):
        return "%s %s" % (self.cluster_id, self.cluster_description)
    class Meta:
        ordering = ('cluster_id',)
        verbose_name = "Cluster Data"
        verbose_name_plural = "Cluster Data"

class ProjectData(models.Model):
    cluster_id = models.ForeignKey(ClusterData, to_field='cluster_id', on_delete=models.CASCADE)
    project_id = models.CharField(max_length=10,unique=True,default=timezone.now)
    project_description = models.CharField(max_length = 200)
    def __str__(self):
        return "%s %s %s" % (self.cluster_id, self.project_id, self.project_description)
    class Meta:
        ordering = ('project_id',)
        verbose_name = "Project Data"
        verbose_name_plural = "Project Data"

class ModuleData(models.Model):
    project_id = models.ForeignKey(ProjectData, to_field='project_id', on_delete=models.CASCADE)
    module_id = models.CharField(max_length=10,unique=True,default=timezone.now)
    module_description = models.CharField(max_length = 200)
    def __str__(self):
        return "%s %s %s" % (self.project_id, self.module_id, self.module_description)
    class Meta:
        ordering = ('module_id',)
        verbose_name = "Module Data"
        verbose_name_plural = "Module Data"

class ErrorData(models.Model):
    module_id = models.ForeignKey(ModuleData, to_field='module_id', on_delete=models.CASCADE)
    error_id = models.CharField(max_length=10,unique=True,default=timezone.now)
    error_description = models.CharField(max_length = 200)
    error_mitigation = models.CharField(max_length = 1000)
    screenshot_link = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    error_validated = models.BooleanField(default=False)
    error_validator = models.CharField(max_length = 200)
    editors_list = models.CharField(max_length = 1000)
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" % (self.module_id, self.error_id, self.error_description,self.error_mitigation,self.screenshot_link,self.author,self.error_validated,self.error_validator,self.editors_list)
    class Meta:
        ordering = ('error_id',)
        verbose_name = "Error Data"
        verbose_name_plural = "Error Data"