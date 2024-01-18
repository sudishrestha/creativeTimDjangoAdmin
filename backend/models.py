from django.db import models

# Create your models here. 

class shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255) 
    class Meta:
        managed = True
        db_table = 'shop' 
class review(models.Model):
    shop_id=  models.ForeignKey(shop, models.DO_NOTHING, db_column='shop_id',related_name='shop') 
    full_name = models.CharField(max_length=255) 
    email = models.CharField(max_length=255) 
    phone = models.CharField(max_length=15) 
    review = models.TextField()
    stars = models.IntegerField() 
    class Meta:
        managed = True
        db_table = 'review' 