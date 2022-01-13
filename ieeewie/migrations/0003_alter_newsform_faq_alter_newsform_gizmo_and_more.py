# Generated by Django 4.0 on 2022-01-13 04:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieeewie', '0002_remove_newsform_image_newsform_image_head_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsform',
            name='faq',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='gizmo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='glossary',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='headlines',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='image_head',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='learning',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='month',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='myth',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='performer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='spot',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='summary',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='timeline',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='womenintech',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsform',
            name='year',
            field=models.CharField(max_length=50),
        ),
    ]
