# Generated by Django 3.1.4 on 2020-12-31 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Warranty_Details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranty_details',
            name='Importance',
            field=models.CharField(choices=[('Critical', 'A'), ('Urgent', 'B'), ('Moderate', 'C'), ('Minor', 'D')], default='Moderate', max_length=10),
        ),
        migrations.AlterField(
            model_name='warranty_details',
            name='section',
            field=models.CharField(choices=[('1', 'Hull'), ('2', 'Machinery'), ('3', 'Painting'), ('4', 'Accommodation'), ('5', 'Design'), ('6', 'Management')], max_length=15),
        ),
    ]
