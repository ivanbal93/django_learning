# Generated by Django 4.2.3 on 2023-08-02 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_city_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='Author', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.author'),
        ),
    ]
