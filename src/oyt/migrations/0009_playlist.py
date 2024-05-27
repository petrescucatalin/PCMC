

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0008_video_is_private'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('video_ids', models.JSONField()),
            ],
        ),
    ]
