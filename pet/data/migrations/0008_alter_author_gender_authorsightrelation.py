# Generated by Django 4.2.3 on 2023-08-02 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_alter_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина'), (None, 'Не указан')], default=None),
        ),
        migrations.CreateModel(
            name='AuthorSightRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.author')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.sight')),
            ],
        ),
    ]
