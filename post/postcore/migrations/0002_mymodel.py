# Generated by Django 3.2.6 on 2021-10-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postcore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='media/')),
            ],
        ),
    ]
