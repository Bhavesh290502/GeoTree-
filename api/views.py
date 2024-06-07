# views.py
from rest_framework import viewsets
from .models import ConditionOpsations, OwnershipOpsations, TreeInfo, TreeImage, TreeData, PrivateOwnerShipDeatils
from .serializers import ConditionOpsationsSerializer, OwnershipOpsationsSerializer, TreeInfoSerializer, TreeImageSerializer, TreeDataSerializer, PrivateOwnerShipDeatilsSerializer

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsPatnerOrReadOnly
from account.renderers import UserRenderer


class ConditionOpsationsViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAdminOrReadOnly]
    queryset = ConditionOpsations.objects.all()
    serializer_class = ConditionOpsationsSerializer

class OwnershipOpsationsViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAdminOrReadOnly]
    queryset = OwnershipOpsations.objects.all()
    serializer_class = OwnershipOpsationsSerializer

class TreeInfoViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAdminOrReadOnly]
    queryset = TreeInfo.objects.all()
    serializer_class = TreeInfoSerializer

class TreeImageViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,)
    renderer_classes = [UserRenderer]
    permission_classes = [IsPatnerOrReadOnly]
    queryset = TreeImage.objects.all()
    serializer_class = TreeImageSerializer

class TreeDataViewSet(viewsets.ModelViewSet):
    # renderer_classes = [UserRenderer]
    permission_classes = [IsPatnerOrReadOnly]
    queryset = TreeData.objects.all()
    serializer_class = TreeDataSerializer
    
    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)
        
class PrivateOwnerShipDeatilsViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserRenderer]
    permission_classes = [IsPatnerOrReadOnly]
    queryset = PrivateOwnerShipDeatils.objects.all()
    serializer_class = PrivateOwnerShipDeatilsSerializer
    