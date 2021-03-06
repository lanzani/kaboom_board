# Generated by Django 3.2.4 on 2021-06-23 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('status', models.CharField(choices=[('p', 'in_progress'), ('a', 'archived')], max_length=1)),
                ('board_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.board')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('creation_date', models.DateTimeField()),
                ('content_type', models.CharField(choices=[('o', 'org'), ('i', 'inf')], max_length=1)),
                ('content', models.TextField()),
                ('multimedia_obj', models.CharField(max_length=45)),
                ('board_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.board')),
                ('column_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.column')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.team')),
            ],
        ),
        migrations.AddField(
            model_name='column',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.team'),
        ),
        migrations.AddField(
            model_name='board',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.team'),
        ),
    ]
