# Generated by Django 2.0.3 on 2018-04-14 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0007_auto_20180414_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='receiver_no',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='item',
            name='sender_no',
            field=models.CharField(max_length=17),
        ),
    ]
