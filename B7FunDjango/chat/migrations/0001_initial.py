# Generated by Django 2.2.11 on 2020-05-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Time sent')),
                ('message', models.TextField(verbose_name='message')),
                ('sender_email', models.EmailField(max_length=60, unique=True, verbose_name='sender email')),
                ('chat_room_id', models.CharField(max_length=30, verbose_name='Chat room id')),
            ],
            options={
                'verbose_name_plural': 'Chat Messages',
            },
        ),
    ]
