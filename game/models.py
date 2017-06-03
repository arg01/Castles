from django.db import models
from django.urls import reverse
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
import django_tables2 as tables
from django.core.exceptions import ValidationError

class players(models.Model):
    name= models.CharField(max_length=40, help_text="Enter a name", unique=True)
    Allocations1 = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Level 1 Castles")
    Allocations2 = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Level 2 Castles")
    Allocations3 = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Level 3 Castles")
    Allocations4 = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Level 4 Castles")
    Allocations5 = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Level 5 Castles")
    Allocations6 = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Level 6 Castles")
    Allocations7 = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Level 7 Castles")
    Allocations8 = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Level 8 Castles")
    Allocations9 = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Level 9 Castles")
    Allocations10 = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Level 10 Castles")
    played = models.BooleanField(default=False)
    display = models.BooleanField(default=False)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)

    def __str__(self):
        return self.name


    ##def clean(self):
    #    total_army = 100
    #    i=1
    #    while i <=10:
    #       allocation=eval('Allocations'+str(i))
    #       total_army -= allocation
    #       if total_percentage !=0:
    ##           raise ValidationError("Army count does not equal 100")
