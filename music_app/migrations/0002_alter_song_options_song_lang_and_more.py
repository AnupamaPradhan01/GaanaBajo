# Generated by Django 5.0.6 on 2024-06-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['-publish']},
        ),
        migrations.AddField(
            model_name='song',
            name='lang',
            field=models.CharField(choices=[('H', 'Hindi'), ('E', 'English')], default='H', max_length=2),
        ),
        migrations.AddIndex(
            model_name='song',
            index=models.Index(fields=['-publish'], name='music_app_s_publish_a9930a_idx'),
        ),
    ]
