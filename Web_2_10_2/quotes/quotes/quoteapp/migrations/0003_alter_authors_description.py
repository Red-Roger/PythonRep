# Generated by Django 5.0.2 on 2024-02-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0002_alter_authors_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='description',
            field=models.CharField(max_length=10000),
        ),
    ]
