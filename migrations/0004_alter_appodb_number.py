# Generated by Django 4.1.7 on 2023-02-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_appodb_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appodb',
            name='Number',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
