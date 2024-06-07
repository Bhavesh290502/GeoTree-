from django.db import models

# Create your models here.

class ConditionOpsations(models.Model):
    Condition = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
      return self.Condition

class OwnershipOpsations(models.Model):
    ownership = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.ownership
  

class TreeInfo(models.Model):
    TreeName = models.CharField(max_length=50)
    BotanicalName = models.CharField(max_length=50)
    Family = models.CharField(max_length=50)
    FlowerColor = models.CharField(max_length=20)
    FruitSeason = models.CharField(max_length=20)
    FlowerSeason = models.CharField(max_length=20)
    ShortDescription = models.TextField(null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
      return self.TreeName

class TreeImage(models.Model):
    TreeImages =  models.ImageField(upload_to='images/' ,default=None, blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

class TreeData(models.Model):
    QrCode = models.CharField(max_length=20,unique=True,primary_key=True)
    TreeImage_id = models.ForeignKey(TreeImage, on_delete=models.CASCADE, related_name="TreeImageUriBy")
    TreeInfo_Id = models.ForeignKey(TreeInfo,on_delete=models.CASCADE , related_name="TreeInfoBy")
    Girth_m = models.IntegerField()
    Height_m = models.IntegerField()
    Age_y = models.IntegerField()
    ConditionInfo_id = models.ForeignKey(ConditionOpsations, on_delete=models.CASCADE, related_name="ConditionBy")
    ownershipinfo_id = models.ForeignKey(OwnershipOpsations, on_delete=models.CASCADE, related_name="OwnershipBy")
    TreeCanopy_m = models.IntegerField()
    Location_Lat = models.CharField(max_length=20)
    Location_Long = models.CharField(max_length=20)
    Remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    submitted_by = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
      return self.QrCode
  
class PrivateOwnerShipDeatils(models.Model):
    PvOwnerShip_QrCode = models.CharField(max_length=20,unique=True,primary_key=True)
    Name = models.CharField(max_length=20, null=True, blank=True)
    Contact_number = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)