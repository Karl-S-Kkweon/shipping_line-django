# Generated by Django 3.1.4 on 2020-12-05 05:23

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hull',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('no', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('delivery_date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hulls', to='owners.Owner')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
