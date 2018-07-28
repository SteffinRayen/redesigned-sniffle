import csv
from sample.models import ClusterData, ProjectData, ModuleData, ErrorData

clusterData = open('~\\DATA\\clusterData.csv','r')
clusterDataRow = list(tuple(rec) for rec in csv.reader(clusterData, delimiter=','))
for element in clusterDataRow:
    currentCluster = ClusterData(
        cluster_id = element[0],
        cluster_description = element[1]
    )
    print (currentCluster)

projectData = open('~\\DATA\\projectData.csv','r')
projectDataRow = list(tuple(rec) for rec in csv.reader(projectData, delimiter=','))
for element in projectDataRow:
    cluster_id, _ = ClusterData.objects.get_or_create(cluster_id=element[0], cluster_description=element[1])
    currentProject = ProjectData (
        cluster_id = cluster_id,
        project_id = element[2],
        project_description = element[3]
    )
    print (currentProject)
    currentProject.save()

moduleData = open('~\\DATA\\moduleData.csv','r')
moduleDataRow = list(tuple(rec) for rec in csv.reader(moduleData, delimiter=','))
for element in moduleDataRow:
    cluster_id, _ = ClusterData.objects.get_or_create(cluster_id=element[0], cluster_description=element[1])
    project_id, _ = ProjectData.objects.get_or_create(cluster_id=cluster_id,project_id=element[2],project_description=element[3])
    currentModule = ModuleData (
        project_id = project_id,
        module_id = element[4],
        module_description = element[5]
    )
    print (currentModule)
    currentModule.save()


errorData = open('~\\DATA\\errorData.csv','r')
errorDataRow = list(tuple(rec) for rec in csv.reader(errorData, delimiter=','))
for element in errorDataRow:
    cluster_id, _ = ClusterData.objects.get_or_create(cluster_id=element[0], cluster_description=element[1])
    project_id, _ = ProjectData.objects.get_or_create(cluster_id=cluster_id,project_id=element[2],project_description=element[3])
    module_id, _ = ModuleData.objects.get_or_create(project_id=project_id, module_id=element[4], module_description=element[5])
    currentError = ErrorData (
        module_id = module_id,
        error_id = element[6], 
        error_description = element[7],
        error_mitigation = element[8],
        screenshot_link = element[9],
        author = element[10],
        error_validated = element[11],
        error_validator = element[12],
        editors_list = element[13]
    )
    print (currentError)
    currentError.save()
