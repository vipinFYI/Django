from importlib.resources import contents
from turtle import title
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# class Article(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     content_upload = RichTextUploadingField(blank=True, null=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    #content =RichTextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    content2 = RichTextUploadingField(blank=True, null=True,config_name = 'special')
    body = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank= True, null=True)
    tags = TaggableManager()

    slug = models.SlugField(default='', blank=True)

    def save(self):
        self.slug = slugify(self.title)
        super(Article,self).save()


    def __str__(self):
        return '%s' % self.title
