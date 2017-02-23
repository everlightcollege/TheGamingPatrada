from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    class Meta:

        db_table = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)




class Games(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=False, null=False)
    name = models.CharField(max_length=50)
    cover_photo = models.ImageField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    requirements = models.TextField(blank=False, null=False)
    download = models.TextField(blank=False, null=False)
    slug = models.SlugField()
    class Meta:
        verbose_name_plural = 'Games'
        db_table = 'Games'

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Games, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

