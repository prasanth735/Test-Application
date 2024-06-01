# Generated by Django 5.0.6 on 2024-05-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dept', models.CharField(max_length=200)),
                ('photo', models.ImageField(default='..', null=True, upload_to='student_imges')),
                ('admission_no', models.CharField(max_length=150)),
            ],
        ),
    ]
