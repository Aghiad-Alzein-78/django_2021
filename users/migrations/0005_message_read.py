# Generated by Django 3.2.5 on 2021-08-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]