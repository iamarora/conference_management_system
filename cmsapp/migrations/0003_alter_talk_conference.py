# Generated by Django 3.2.7 on 2021-09-10 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0002_auto_20210910_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talk', to='cmsapp.conference'),
        ),
    ]
