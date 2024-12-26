# Generated by Django 5.1.4 on 2024-12-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_alter_pet_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not Informed', 'Informed')], default='Not Informed', max_length=20),
        ),
    ]