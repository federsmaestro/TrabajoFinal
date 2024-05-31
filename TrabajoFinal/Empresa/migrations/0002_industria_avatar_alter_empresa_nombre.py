# Generated by Django 5.0.6 on 2024-05-31 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='industria',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
