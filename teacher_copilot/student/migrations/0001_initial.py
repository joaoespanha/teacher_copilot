# Generated by Django 4.2.3 on 2023-08-29 04:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guardian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('favorite_subject', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=20)),
                ('notes', models.TextField(max_length=500)),
                ('birthday', models.DateField()),
                ('football_team', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, upload_to='student_photos')),
                ('instagram', models.CharField(max_length=50)),
                ('guardians', models.ManyToManyField(related_name='students', to='guardian.guardian')),
                ('teacher', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
