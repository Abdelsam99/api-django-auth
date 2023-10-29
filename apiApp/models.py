from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    content=models.TextField(null=True, blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    
    class Meta:
        verbose_name=('Product')
        verbose_name_plural = ("Products")
        
    def __str__(self):
        return self.name