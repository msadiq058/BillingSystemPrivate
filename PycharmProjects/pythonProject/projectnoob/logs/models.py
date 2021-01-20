from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Firm(models.Model):
    firm_name = models.CharField(max_length = 200,primary_key=True,unique=True)
    gstin = models.CharField(max_length= 15,blank=True)
    date = models.DateField(editable=False,default=timezone.now)
    def __str__(self):
        return self.firm_name

    def clean(self):
        self.firm_name = self.firm_name.upper()
        auto_now_add = False
        # self.date = timezone.now
    
    class Meta:
        ordering = ['firm_name']

class Entry(models.Model):
    firm_name = models.ForeignKey(Firm,on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    size_range = [
        ('1.0','1.0'),
        ('1.5','1.5'),
        ('2.0','2.0'),
        ('2.5','2.5'),
        ('3.0','3.0'),
        ('4.0','4.0'),
        ('5.0','5.0'),
        ('6.0','6.0'),
    ]
    size = models.CharField(max_length = 3,choices=size_range)
    weight = models.DecimalField(max_digits = 10 , decimal_places=3,validators=[
        MinValueValidator(1)
    ])
    quantity = models.IntegerField(default=0)
    making = (
        (u'Framed',u'Framed'),
        (u'Sticked',u'Sticked')
    )
    making_type = models.CharField(max_length=10,choices=making)
    remarks = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return str(self.firm_name)