# Generated by Django 4.1.4 on 2022-12-28 14:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('score_one', models.IntegerField(default=0)),
                ('score_two', models.IntegerField(default=0)),
                ('level_price', models.DecimalField(decimal_places=2, default=4.99, max_digits=7)),
                ('date_time', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Matches',
                'db_table': 'matches',
            },
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'referees',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('row', models.IntegerField()),
                ('seat', models.IntegerField()),
            ],
            options={
                'db_table': 'seats',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('rows_num', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(26)])),
                ('seats_num', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'db_table': 'venues',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.match')),
            ],
            options={
                'db_table': 'tickets',
            },
        ),
    ]
