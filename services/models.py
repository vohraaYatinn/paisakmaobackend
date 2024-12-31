from django.db import models
from authentication.models import User

# Create your models here.
class ServicesType(models.Model):
    service_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service_name}'


class ServicesWorking(models.Model):
    service_name = models.ForeignKey(ServicesType, on_delete=models.CASCADE, related_name='services_working')
    company_name = models.CharField(max_length=50)
    earnings = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    link = models.TextField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service_name} - {self.company_name} - {self.id}'


class ServiceDetails(models.Model):
    service_name = models.ForeignKey(ServicesWorking, on_delete=models.CASCADE, related_name='services_working')
    description = models.TextField()
    link = models.TextField()

    def __str__(self):
        return f'{self.service_name} - {self.description[:10]}'