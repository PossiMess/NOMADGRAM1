# Generated by Django 2.0.10 on 2019-03-25 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20190319_1051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at']},
        ),
    ]
