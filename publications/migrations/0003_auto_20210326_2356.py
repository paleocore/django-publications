# Generated by Django 2.2.19 on 2021-03-26 23:56
# update

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='doi',
            field=models.CharField(blank=True, help_text='e.g. 10.1073/pnas.2006221117', max_length=128, verbose_name='DOI'),
        ),
    ]
