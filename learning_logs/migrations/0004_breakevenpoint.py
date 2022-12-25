# Generated by Django 4.1.3 on 2022-12-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakEvenPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_cost', models.DecimalField(decimal_places=2, max_digits=250)),
                ('reg_price', models.DecimalField(decimal_places=2, max_digits=250)),
                ('disc_price', models.DecimalField(decimal_places=2, max_digits=250)),
            ],
        ),
    ]
