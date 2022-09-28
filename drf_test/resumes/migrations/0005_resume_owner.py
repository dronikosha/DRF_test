# Generated by Django 4.1.1 on 2022-09-28 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resumes', '0004_remove_resume_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]