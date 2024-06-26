# Generated by Django 4.1.4 on 2024-03-29 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('startdate', models.DateField(blank=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
