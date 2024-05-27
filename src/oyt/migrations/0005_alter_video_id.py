

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyt', '0004_auto_20210408_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
