from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Newsform(models.Model):
    month=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    glossary=RichTextField(blank=True, null=True)
    headlines=RichTextField(blank=True, null=True)
    timeline=RichTextField(blank=True, null=True)
    womenintech=RichTextField(blank=True, null=True)
    learning=RichTextField(blank=True, null=True)
    myth=RichTextField(blank=True, null=True)
    gizmo=RichTextField(blank=True, null=True)
    summary=RichTextField(blank=True, null=True)
    faq=RichTextField(blank=True, null=True)
    spot=RichTextField(blank=True, null=True)
    performer=RichTextField(blank=True, null=True)
    image_head=models.ImageField(null=True, blank=True, upload_to="media")
    #pdf=models.FileField(max_length=50)
    
    def __str__(self):
        return self.month + ' ' + self.year
