from django.db import models

# Create your models here.


class Company(models.Model):
    company_id = models.CharField(max_length=255, primary_key=True)
    company_name = models.CharField(max_length=255)


class Simulation(models.Model):
    simulation_id = models.CharField(max_length=255, primary_key=True)
    simulation_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class User(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    user_name = models.CharField(max_length=255)
    user_surname = models.CharField(max_length=255)
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)
    signup_datetime = models.DateTimeField()
    progress_percent = models.FloatField()

