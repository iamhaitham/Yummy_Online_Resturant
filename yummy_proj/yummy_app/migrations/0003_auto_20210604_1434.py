# Generated by Django 3.2.3 on 2021-06-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummy_app', '0002_auto_20210603_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
