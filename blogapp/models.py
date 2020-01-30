from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class author(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    details=models.TextField()
    def __str__(self):
        return self.name.username

class article(models.Model):
    article_author=models.ForeignKey(author,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    title1=models.CharField(max_length=100)
    body=RichTextField()
    body1 = RichTextField()
    image = models.FileField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title

class content(models.Model):
    article_author=models.ForeignKey(author,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)

    body=models.TextField()
    image = models.FileField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title
class livingcost(models.Model):
    article_author=models.ForeignKey(author,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)

    body = RichTextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title
class earning(models.Model):
    article_author=models.ForeignKey(author,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)

    body = RichTextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title
class embassy_address(models.Model):
    article_author=models.ForeignKey(author,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)

    body = RichTextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title
class ticket_price(models.Model):
    article_author=models.ForeignKey(author,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)

    body = RichTextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title
class Contatct(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.fname
class subscribe(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email