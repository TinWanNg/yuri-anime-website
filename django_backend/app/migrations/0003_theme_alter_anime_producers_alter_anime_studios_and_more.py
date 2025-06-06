# Generated by Django 5.1.2 on 2025-06-06 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_yurianime_anime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='anime',
            name='producers',
            field=models.ManyToManyField(null=True, related_name='animes', to='app.producer'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='studios',
            field=models.ManyToManyField(null=True, related_name='animes', to='app.studio'),
        ),
        migrations.RemoveField(
            model_name='anime',
            name='themes',
        ),
        migrations.AddField(
            model_name='anime',
            name='themes',
            field=models.ManyToManyField(null=True, related_name='animes', to='app.theme'),
        ),
    ]
