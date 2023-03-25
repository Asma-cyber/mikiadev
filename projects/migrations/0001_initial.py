# Generated by Django 4.1.7 on 2023-03-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('display_name', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('picture', models.ImageField(upload_to='project_pictures/')),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
