# Generated by Django 4.1.4 on 2023-06-15 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskomatic', '0010_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=280)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskomatic.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
