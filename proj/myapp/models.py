from django.db import models

# Create your models here.


class Module(models.Model):

    factory_number = models.CharField(primary_key=True, max_length=30) # 3D/526 3D/527
    revision = models.FloatField(null=True, blank=True)
    module_name = models.CharField(null=True, max_length=30)
    consignment_number = models.IntegerField(null=True, blank=True)
    manufacturer = models.CharField(max_length=30, blank=True)
    production_date = models.DateField(null=True, blank=True)
    qc_pass_date = models.DateField(null=True, blank=True)
    hash = models.TextField(blank=True)
    engineer_name = models.CharField(max_length=30, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f'{self.module_name}/{self.factory_number}'
        

class Controller(models.Model):
    factory_number = models.CharField(primary_key=True, max_length=30)
    manufacturing_request_number = models.CharField(max_length=30, blank=True)
    controller_type = models.CharField(null=True, max_length=30)
    another_equipment_numbers = models.CharField(max_length=30, blank=True)
    controller_production_date = models.DateField(null=True, blank=True)
    qc_date = models.DateField(null=True, blank=True)
    metrology_check = models.NullBooleanField(blank=True)
    project_name = models.CharField(max_length=30, blank=True)
    project_manager_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.controller_type}/{self.factory_number}'


class ControllerModule(models.Model):
    module = models.ForeignKey('Module', unique=True, on_delete=models.CASCADE)
    controller = models.ForeignKey('Controller', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('module', 'controller'),)

    def __str__(self):
        return f'{self.controller}-{self.module}'


class Slot(models.Model):
    controller_module = models.ForeignKey('ControllerModule', unique=True, on_delete=models.CASCADE)
    slot_number = models.IntegerField(editable=True)

    class Meta:
        unique_together = (('slot_number', 'controller_module'),)

    def __str__(self):
        return f'{self.controller_module}-{self.slot_number}'

