# Generated by Django 3.0.2 on 2021-04-04 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_deliveryitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
