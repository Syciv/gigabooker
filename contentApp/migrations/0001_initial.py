# Generated by Django 3.2.8 on 2021-11-05 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth', models.DateField(blank=True, null=True)),
                ('death', models.DateField(blank=True, null=True)),
                ('information', models.TextField(default='Пока ничего нет')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('information', models.TextField(default='Пока ничего нет')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contentApp.authors')),
            ],
        ),
    ]