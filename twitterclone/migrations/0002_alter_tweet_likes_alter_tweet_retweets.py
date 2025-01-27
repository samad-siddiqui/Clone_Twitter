# Generated by Django 5.1 on 2024-08-31 08:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_tweets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweets',
            field=models.ManyToManyField(blank=True, related_name='retweeted_tweets', to=settings.AUTH_USER_MODEL),
        ),
    ]
