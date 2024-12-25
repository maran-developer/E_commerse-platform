from django.db import models
from django.contrib.auth.models import User
import datetime
import os

from django.db.models import CASCADE
from django.db.transaction import mark_for_rollback_on_error


def getFileName(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M%S")
    new_filename ="%s%s"%(now_time,filename)
    return os.path.join('upload/',new_filename)

class category(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=False,blank=False)
    description=models.TextField(max_length=400,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,null=False,blank=False)
    vendor=models.CharField(max_length=20,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=False,blank=False)
    quentity = models.IntegerField(null=False, blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=400,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    product=models.ForeignKey(product,on_delete=CASCADE)
    product_quentity=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_quentity*self.product.selling_price

class favourite(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    product=models.ForeignKey(product,on_delete=CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)