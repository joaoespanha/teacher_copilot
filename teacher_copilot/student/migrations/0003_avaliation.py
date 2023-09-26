# Generated by Django 4.2.3 on 2023-09-26 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('revised', models.BooleanField(default=False)),
                ('notes', models.TextField(max_length=500)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliations', to='student.student')),
            ],
        ),
    ]
