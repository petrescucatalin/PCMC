

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0003_alter_video_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='path',
            field=models.CharField(max_length=1000),
        ),
    ]
