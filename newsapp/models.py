from django.db import models
from django.contrib.auth.models import AbstractUser


class Customeuser(AbstractUser):
    USER={
        (1,'admin'),
        (2,'subadmin')
    }
    user_type=models.CharField(choices=USER,default=1,max_length=100)
    profile_pic = models.ImageField(upload_to='media/profileimage')

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    category_description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.category_name
    
class Subcategory(models.Model):
    cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category_name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sub_category_name
    
class News(models.Model):
    cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_id=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    newstitle=models.TextField(blank=True)
    newsdetails=models.TextField(blank=True)
    newsimage=models.ImageField(upload_to='media/news')
    status=models.CharField(max_length=100)
    news_post_date=models.DateTimeField(auto_now_add=True)
    news_update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.newstitle

class Comments(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    status = models.CharField(max_length=250,blank=True)
    posted_date= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)