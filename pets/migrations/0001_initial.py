# Generated by Django 5.1.4 on 2024-12-26 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('traits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('weight', models.FloatField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not Informed', 'Not Informed')], default='Not Informed', max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pets', to='groups.group')),
                ('traits', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='traits.trait')),
            ],
        ),
    ]
