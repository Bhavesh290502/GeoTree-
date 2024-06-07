from django.contrib import admin
from .models import ConditionOpsations, OwnershipOpsations, TreeInfo, TreeImage, TreeData

@admin.register(ConditionOpsations)
class ConditionOpsationsAdmin(admin.ModelAdmin):
    list_display = ('Condition',)
    search_fields = ('Condition',)

@admin.register(OwnershipOpsations)
class OwnershipOpsationsAdmin(admin.ModelAdmin):
    list_display = ('ownership',)
    search_fields = ('ownership',)

@admin.register(TreeInfo)
class TreeInfoAdmin(admin.ModelAdmin):
    list_display = ('TreeName', 'BotanicalName', 'Family', 'FruitSeason', 'FlowerSeason')
    search_fields = ('TreeName', 'BotanicalName', 'Family')
    list_filter = ('FruitSeason', 'FlowerSeason')

@admin.register(TreeImage)
class TreeImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'TreeImages')
    # Add search fields or filters if necessary

@admin.register(TreeData)
class TreeDataAdmin(admin.ModelAdmin):
    list_display = ('QrCode', 'TreeImage_id', 'TreeInfo_Id', 'Girth_m', 'Height_m', 'Age_y', 'ConditionInfo_id', 'ownershipinfo_id', 'TreeCanopy_m', 'Location_Lat', 'Location_Long', 'Remarks')
    search_fields = ('QrCode', 'TreeInfo_Id__TreeName', 'Location_Lat', 'Location_Long')
    list_filter = ('ConditionInfo_id', 'ownershipinfo_id', 'Age_y')

    def TreeImage_id(self, obj):
        return obj.TreeImage_id.TreeImages

    def TreeInfo_Id(self, obj):
        return obj.TreeInfo_Id.TreeName

    def ConditionInfo_id(self, obj):
        return obj.ConditionInfo_id.Condition

    def ownershipinfo_id(self, obj):
        return obj.ownershipinfo_id.ownership
