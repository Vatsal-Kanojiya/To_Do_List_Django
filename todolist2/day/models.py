# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify




class activity(models.Model):
    order=models.IntegerField(validators=[MinValueValidator(1)])
    task=models.CharField(max_length=50,null=False)
    status=models.BooleanField(default=False, null=False)
    day=models.IntegerField(null=False,default=11,validators=[MinValueValidator(1),MaxValueValidator(31)])
    month=models.IntegerField(null=False,default=11,validators=[MinValueValidator(1),MaxValueValidator(12)])
    year=models.IntegerField(null=False,default=2023,validators=[MinValueValidator(1950),MaxValueValidator(2050)])
    slug=models.SlugField(default='slugdefault',null=False,blank=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.task)
        return super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.task}"