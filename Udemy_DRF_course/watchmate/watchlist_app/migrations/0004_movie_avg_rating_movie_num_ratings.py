# Generated by Django 4.0.3 on 2022-06-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0003_rename_reviewer_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=30),
        ),
        migrations.AddField(
            model_name='movie',
            name='num_ratings',
            field=models.IntegerField(default=0),
        ),
    ]