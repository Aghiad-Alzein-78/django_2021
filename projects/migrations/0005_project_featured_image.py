# Generated by Django 3.2.5 on 2021-07-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_votes_ratio'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
