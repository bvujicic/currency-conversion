# Generated by Django 2.0.1 on 2018-01-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('eur_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='euro amount')),
                ('conversion_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='conversion_rate')),
                ('request_ip', models.GenericIPAddressField(verbose_name='request IP')),
            ],
            options={
                'db_table': 'euro_coversion',
            },
        ),
    ]
