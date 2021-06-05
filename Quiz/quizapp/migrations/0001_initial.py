# Generated by Django 3.2.3 on 2021-05-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(default=None, max_length=200)),
                ('option4', models.CharField(default=None, max_length=200)),
                ('option5', models.CharField(default=None, max_length=200)),
                ('answer', models.IntegerField()),
                ('subject', models.CharField(max_length=20)),
            ],
        ),
    ]