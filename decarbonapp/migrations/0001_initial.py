# Generated by Django 4.0 on 2022-05-31 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gmail', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]