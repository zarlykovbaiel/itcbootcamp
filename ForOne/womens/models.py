from django.db import models


class Women(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
