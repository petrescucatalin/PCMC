
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0011_alter_playlist_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
