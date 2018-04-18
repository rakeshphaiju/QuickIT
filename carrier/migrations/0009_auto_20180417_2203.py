# Generated by Django 2.0.3 on 2018-04-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0008_auto_20180414_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='dropoff_place',
            field=models.CharField(default='SOME STRING', max_length=300),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='pickup_place',
            field=models.CharField(default='SOME STRING', max_length=300),
        ),
        migrations.AlterField(
            model_name='item',
            name='receiver_name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='receiver_no',
            field=models.CharField(default='SOME STRING', max_length=17),
        ),
        migrations.AlterField(
            model_name='item',
            name='sender_name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='sender_no',
            field=models.CharField(blank=True, default='SOME STRING', max_length=17, null=True),
        ),
    ]
