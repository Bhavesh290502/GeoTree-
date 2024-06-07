# serializers.py
from rest_framework import serializers
from .models import ConditionOpsations, OwnershipOpsations, TreeInfo, TreeImage, TreeData, PrivateOwnerShipDeatils

class ConditionOpsationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionOpsations
        fields = '__all__'

class OwnershipOpsationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnershipOpsations
        fields = '__all__'

class TreeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeInfo
        fields = '__all__'

class TreeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeImage
        fields = '__all__'

class TreeDataSerializer(serializers.ModelSerializer):
    TreeImage_id = TreeImageSerializer(read_only=True)
    TreeImage_id_by = serializers.PrimaryKeyRelatedField(queryset=TreeImage.objects.all(), source='TreeImage_id', write_only=True)
    
    TreeInfo_Id = TreeInfoSerializer(read_only=True)
    TreeInfo_Id_by = serializers.PrimaryKeyRelatedField(queryset=TreeInfo.objects.all(), source='TreeInfo_Id', write_only=True)
    
    ConditionInfo_id = ConditionOpsationsSerializer(read_only=True)
    ConditionInfo_id_by = serializers.PrimaryKeyRelatedField(queryset=ConditionOpsations.objects.all(), source='ConditionInfo_id', write_only=True)
    
    ownershipinfo_id = OwnershipOpsationsSerializer(read_only=True)
    ownershipinfo_id_by = serializers.PrimaryKeyRelatedField(queryset=OwnershipOpsations.objects.all(), source='ownershipinfo_id', write_only=True)
    
    class Meta:
        model = TreeData
        fields = ['QrCode', 'TreeImage_id', 'TreeInfo_Id', 'Girth_m', 'Height_m', 'Age_y',
                  'TreeCanopy_m', 'Location_Lat', 'Location_Long', 'Remarks', 'submitted_by',
                  'ConditionInfo_id', 'ownershipinfo_id','TreeImage_id_by','TreeInfo_Id_by','ConditionInfo_id_by','ownershipinfo_id_by']
        
class PrivateOwnerShipDeatilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateOwnerShipDeatils
        fields = '__all__'