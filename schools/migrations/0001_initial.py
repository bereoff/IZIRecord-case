# Generated by Django 4.2.6 on 2023-10-12 17:22

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('created_at', models.DateTimeField(
                    auto_created=True, auto_now_add=True, db_index=True)),
                ('id', models.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),  # NOQA
                ('name', models.CharField(blank=True, max_length=255, null=True)),  # NOQA
                ('maximum_capacity', models.IntegerField(blank=True, null=True)),  # NOQA
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
