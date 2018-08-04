import csv
from sample.models import ClusterData, ProjectData, ModuleData, ErrorData

clusterData = open('F:\\GIT_WORKSPACE\\redesignedSniffle\\DATA\\clusterData.csv','r')
clusterDataRow = list(tuple(rec) for rec in csv.reader(clusterData, delimiter=','))
for element in clusterDataRow:
    currentCluster = ClusterData(
        cluster_id = element[0],
        cluster_name = element[1],
        cluster_description = element[2],
    )
    print (currentCluster)

projectData = open('F:\\GIT_WORKSPACE\\redesignedSniffle\\DATA\\projectData.csv','r')
projectDataRow = list(tuple(rec) for rec in csv.reader(projectData, delimiter=','))
for element in projectDataRow:
    cluster_id, _ = ClusterData.objects.get_or_create(cluster_id=element[0], cluster_name=element[1], cluster_description=element[2])
    currentProject = ProjectData (
        cluster_id = cluster_id,
        project_id = element[3],
        project_name = element[4],
        project_description = element[5],
    )
    print (currentProject)
    currentProject.save()

moduleData = open('F:\\GIT_WORKSPACE\\redesignedSniffle\\DATA\\moduleData.csv','r')
moduleDataRow = list(tuple(rec) for rec in csv.reader(moduleData, delimiter=','))
for element in moduleDataRow:
    cluster_id, _ = ClusterData.objects.get_or_create(cluster_id=element[0], cluster_name=element[1], cluster_description=element[2])
    project_id, _ = ProjectData.objects.get_or_create(cluster_id=cluster_id,project_id=element[3],project_name=element[4],project_description=element[5])
    currentModule = ModuleData (
        project_id = project_id,
        module_id = element[6],
        module_name = element[7],
        module_description = element[8]
    )
    print (currentModule)
    currentModule.save()


errorData = open('F:\\GIT_WORKSPACE\\redesignedSniffle\\DATA\\errorData.csv','r')
errorDataRow = list(tuple(rec) for rec in csv.reader(errorData, delimiter=','))
for element in errorDataRow:
    cluster_id, _ = ClusterData.objects.get_or_create(cluster_id=element[0], cluster_name=element[1], cluster_description=element[2])
    project_id, _ = ProjectData.objects.get_or_create(cluster_id=cluster_id,project_id=element[3],project_name=element[4],project_description=element[5])
    module_id, _ = ModuleData.objects.get_or_create(project_id=project_id, module_id=element[6], module_name=element[7], module_description=element[8])
    currentError = ErrorData (
        module_id = module_id,
        error_id = element[9], 
        error_name = element[10],
        error_description = element[11],
        error_mitigation = element[12],
        link_valid = element[13],
        screenshot_link = element[14],
        author = element[15],
        error_validated = element[16],
        error_validator = element[17],
        editors_list = element[18],
    )
    print (currentError)
    currentError.save()
