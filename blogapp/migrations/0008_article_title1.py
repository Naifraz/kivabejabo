# Generated by Django 2.1.3 on 2019-06-14 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title1',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
