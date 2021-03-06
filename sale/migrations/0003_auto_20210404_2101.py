# Generated by Django 3.0.2 on 2021-04-04 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image_link',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
