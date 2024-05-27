
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0015_auto_20210411_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='num_likes',
            field=models.IntegerField(default=0),
        ),
    ]
