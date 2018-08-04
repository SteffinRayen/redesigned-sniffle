# Generated by Django 2.0.7 on 2018-08-03 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='clusterdata',
            name='cluster_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='errordata',
            name='error_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moduledata',
            name='module_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectdata',
            name='project_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clusterdata',
            name='cluster_description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='errordata',
            name='author',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='errordata',
            name='error_description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='errordata',
            name='error_validator',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='errordata',
            name='screenshot_link',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='moduledata',
            name='module_description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='projectdata',
            name='project_description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user_id',
            field=models.CharField(max_length=1000),
        ),
    ]
