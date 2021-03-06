# Generated by Django 2.2.2 on 2019-06-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc_code', models.CharField(max_length=30)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(max_length=30)),
                ('bank_address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('bank_name', models.TextField()),
            ],
        ),
    ]
