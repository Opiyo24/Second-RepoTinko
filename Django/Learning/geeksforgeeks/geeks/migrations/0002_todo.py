# Generated by Django 3.2.12 on 2024-04-28 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]