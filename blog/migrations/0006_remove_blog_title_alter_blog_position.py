# Generated by Django 4.1.4 on 2024-03-29 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
        migrations.AlterField(
            model_name='blog',
            name='position',
            field=models.CharField(max_length=50),
        ),
    ]