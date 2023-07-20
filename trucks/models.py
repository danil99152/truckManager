from django.db import models


class TruckModel(models.Model):
    name = models.CharField(max_length=50)
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Truck(models.Model):
    number = models.CharField(max_length=10)
    model = models.ForeignKey(TruckModel, on_delete=models.CASCADE)
    current_load = models.IntegerField()

    def overload_percent(self):
        return round(self.current_load / self.model.max_capacity * 100) - 100

    def __str__(self):
        return self.number
