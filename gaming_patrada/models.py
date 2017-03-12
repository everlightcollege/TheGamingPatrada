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
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    name = models.TextField(blank=True, null=True, max_length=1000)  # This field type is a guess.
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', )
    release = models.DateField(default='1800-5-5')
    cover_photo = models.CharField(blank=True, null=True, max_length=1000)
    description = models.CharField(blank=True, null=True, max_length=1000)
    requirements = models.CharField(blank=True, null=True, max_length=1000)
    download = models.CharField(blank=True, null=True, max_length=1000)
    slug = models.SlugField(default=1)
    rating = models.DecimalField(decimal_places=5,max_digits=10)
    class Meta:
        managed = True
        db_table = 'Games'
        verbose_name_plural = 'Games'


    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Games, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Letters(models.Model):
    letter = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'letters'
        verbose_name_plural='letters'
