from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Order(models.Model):
    starter = models.TextField()
    main = models.TextField()
    desserts = models.TextField()
    drinks = models.TextField()
    TableInfo = models.TextField()
    CustName = models.TextField()
    RestName = models.TextField()
    bill = models.TextField()
    Table_state = models.TextField()
    dateTimeOrdered = models.DateTimeField(default=timezone.now)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.CustName
    
    def get_absolute_url(self):
        return reverse('orders-detail', kwargs={'pk':self.pk})
