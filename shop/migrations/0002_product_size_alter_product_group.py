# Generated by Django 4.1.5 on 2023-02-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='One size', max_length=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('skates', 'skates'), ('shoes', 'shoes'), ('clothes', 'clothes'), ('accessories', 'accessories')], default='clothes', max_length=20),
        ),
    ]
