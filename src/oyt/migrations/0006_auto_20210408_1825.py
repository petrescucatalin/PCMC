

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0005_alter_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]