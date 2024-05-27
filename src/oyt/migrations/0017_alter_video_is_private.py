
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0016_video_num_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
