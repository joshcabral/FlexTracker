# Generated by Django 2.1.2 on 2018-11-14 06:38

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='flex_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_plan', models.CharField(max_length=256)),
                ('current_flex', models.FloatField()),
                ('access_key', models.CharField(default='', max_length=10)),
                ('phone_number', models.BigIntegerField(null=True)),
                ('service_provider', models.CharField(choices=[('Alltel', 'message.alltel.com'), ('AT&T', 'txt.att.net'), ('Boost Mobile', 'myboostmobile.com'), ('Cricket Wireless', 'sms.cricketwireless.net'), ('Project Fi', 'msg.fi.google.com'), ('Republic Wireless', 'text.republicwireless.com'), ('Sprint', 'messaging.sprintpcs.com'), ('U.S. Cellular', 'tmomail.net'), ('Verizon', 'email.uscc.net'), ('Virgin Mobile', 'vtext.com'), ('UNKNOWN', 'UNKNOWN')], default='UNKNOWN', max_length=50)),
                ('email_notification', models.BooleanField(default=False)),
                ('text_notification', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='flex_transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=256)),
                ('transaction_type', models.CharField(max_length=256)),
                ('transaction_amount', models.FloatField()),
                ('balance', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product_info',
            fields=[
                ('barcode', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('price', models.FloatField()),
                ('location', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]