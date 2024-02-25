# Generated by Django 4.2.10 on 2024-02-25 04:59

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('status', models.CharField(choices=[('on', 'online'), ('off', 'offline')], default='off', max_length=50)),
                ('residence_id', models.CharField(help_text='Enter a name or number of your residence', max_length=30)),
                ('residency', models.CharField(help_text='Enter your society or apartment name', max_length=30)),
                ('street', models.CharField(help_text='Enter your street name', max_length=30)),
                ('area', models.CharField(help_text='Enter your area of city', max_length=30)),
                ('pincode', models.CharField(help_text='Enter your\xa0postal\xa0code', max_length=6, validators=[django.core.validators.RegexValidator(message='Pincode must be of 6 digits', regex='^\\d{6}$')])),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('user.account',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tiffin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
                ('end_time', models.TimeField()),
                ('max_quantity_available', models.PositiveIntegerField()),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.kitchen')),
            ],
        ),
        migrations.CreateModel(
            name='TiffinItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TiffinItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('qty_per_tiffin', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.tiffinitemcategory')),
                ('tiffin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.tiffin')),
            ],
        ),
    ]