# Generated by Django 4.1.4 on 2024-03-28 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0011_alter_experience_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='url',
            new_name='code',
        ),
        migrations.AddField(
            model_name='experience',
            name='demo',
            field=models.URLField(blank=True),
        ),
    ]