

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oyt', '0009_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='is_private',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='name',
            field=models.CharField(default='Deafult-Playlist-Name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
