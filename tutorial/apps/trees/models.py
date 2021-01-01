from django.db import models
from django.utils.timezone import now


class Region(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="department_region")

    def __str__(self):
        return self.name


class TreePlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class TreeHeightReport(models.Model):
    tree_plan = models.ForeignKey(TreePlan, on_delete=models.CASCADE)
    height_0_0_2_count = models.FloatField(verbose_name="0,2 м гача", null=True, blank=True)
    height_0_2_5_count = models.FloatField(verbose_name="0,2 дан 0,5 м гача", null=True, blank=True)
    height_0_5_1_count = models.FloatField(verbose_name="0,5 -1 м. гача", null=True, blank=True)
    height_1_1_5_count = models.FloatField(verbose_name="1-1,5 м гача", null=True, blank=True)
    height_1_5_2_count = models.FloatField(verbose_name="1,5-2 м гача", null=True, blank=True)
    date = models.DateTimeField(default=now)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"Tree: {self.tree_plan} | Region:  {self.region.name}"
