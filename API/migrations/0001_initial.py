# Generated by Django 3.1.7 on 2021-04-16 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eatery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('url', models.CharField(max_length=60)),
                ('eatery_type', models.TextField(choices=[('res', 'Restaurant'), ('din', 'Dining Hall')])),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('url', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('numeric_review', models.IntegerField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Average'), (2, 'Meh'), (1, 'Yuck')])),
                ('eatery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.eatery')),
            ],
        ),
        migrations.AddField(
            model_name='eatery',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.school'),
        ),
    ]
