
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0012_auto_20210411_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='num_likes',
            field=models.IntegerField(default=0),
        ),
    ]
