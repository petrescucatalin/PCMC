
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oyt', '0013_auto_20210411_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='num_likes',
        ),
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(related_name='video_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
