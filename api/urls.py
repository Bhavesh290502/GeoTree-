# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConditionOpsationsViewSet, OwnershipOpsationsViewSet, TreeInfoViewSet, TreeImageViewSet, TreeDataViewSet, PrivateOwnerShipDeatilsViewSet

router = DefaultRouter()
router.register(r'conditionoptions', ConditionOpsationsViewSet)
router.register(r'ownershipoptions', OwnershipOpsationsViewSet)
router.register(r'treeinfo', TreeInfoViewSet)
router.register(r'treeimage', TreeImageViewSet)
router.register(r'treedata', TreeDataViewSet)
router.register(r'PrivateOwnerShipDeatils',PrivateOwnerShipDeatilsViewSet )

urlpatterns = [
    path('', include(router.urls)),
]
