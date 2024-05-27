
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0014_auto_20210411_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
    ]
