from django.db import models

# Create your models here.

class CurrencyConversionRate(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=5)
    last_updated = models.DateTimeField(auto_now=True)
    
    