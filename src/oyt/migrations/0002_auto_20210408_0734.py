
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
