

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0006_auto_20210408_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
