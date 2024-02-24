# Generated by Django 4.2.10 on 2024-02-24 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('foodie', '0002_initial'),
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersummary',
            name='foodie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodie.foodie'),
        ),
        migrations.AddField(
            model_name='orderedtiffin',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.ordersummary'),
        ),
        migrations.AddField(
            model_name='orderedtiffin',
            name='tiffin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.tiffin'),
        ),
    ]
