# Generated by Django 4.2.3 on 2023-08-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_content_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='topics',
            field=models.CharField(choices=[('Baby Development', 'Baby Development'), ('Baby Health', 'Baby Health'), ('Parent Health', 'Parent Health')], max_length=30),
        ),
    ]