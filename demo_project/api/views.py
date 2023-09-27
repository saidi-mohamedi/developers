
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from demoApp.models import Project
from .serializers import ProjectSerializers 


@api_view(['GET'])
def getRoutes(request):
    project = Project.objects.all()
    serializer = ProjectSerializers(project, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def getRoute(request,pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializers(project, many=False)
    return Response(serializer.data)