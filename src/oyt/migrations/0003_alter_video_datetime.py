

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0002_auto_20210408_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='datetime',
            field=models.DateField(auto_now=True),
        ),
    ]
