# Generated by Django 5.0 on 2024-01-03 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('logo_path', models.CharField(blank=True, max_length=255, null=True)),
                ('provider_name', models.CharField(blank=True, max_length=255, null=True)),
                ('provider_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('overview', models.TextField(blank=True, null=True)),
                ('poster_path', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=20, null=True)),
                ('runtime', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('free', models.BooleanField(default=False)),
                ('actors', models.ManyToManyField(to='movies.actors')),
                ('genres', models.ManyToManyField(to='movies.genre')),
                ('buy', models.ManyToManyField(related_name='buy_provider', to='movies.providers')),
                ('rent', models.ManyToManyField(related_name='rent_provider', to='movies.providers')),
            ],
        ),
    ]
