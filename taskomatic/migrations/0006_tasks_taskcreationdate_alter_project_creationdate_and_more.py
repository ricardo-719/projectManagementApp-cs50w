# Generated by Django 4.1.4 on 2023-05-06 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskomatic', '0005_tasks_taskcreator'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='taskCreationDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='creationDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='taskImportance',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=(1, 1), validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]