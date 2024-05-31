from django.db import models

# Create your models here.
class User(models.Model):
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_type = models.CharField(max_length=50)
    user_budget = models.DecimalField(max_digits=13, decimal_places=3, default=0.000)
    
    def __str__(self) :
        return self.user_first_name