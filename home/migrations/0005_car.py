# Generated by Django 5.0.7 on 2024-07-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_student_file_remove_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('speed', models.IntegerField(default=50)),
            ],
        ),
    ]
