# Generated by Django 4.2.3 on 2023-08-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_author_name_alter_review_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
