# Generated by Django 5.1.4 on 2024-12-26 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('pets', '0004_alter_pet_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pets', to='groups.group'),
        ),
    ]
