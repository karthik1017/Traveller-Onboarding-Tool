# Generated by Django 2.1.7 on 2019-03-22 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('one_time_password', models.CharField(blank=True, max_length=6, null=True)),
                ('last_login', models.DateTimeField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='modification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(blank=True, max_length=6, null=True)),
                ('client_id', models.CharField(blank=True, max_length=6, null=True)),
                ('passport_number', models.CharField(blank=True, max_length=6, null=True)),
                ('action_done', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='stafflogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=10, null=True)),
                ('password', models.CharField(blank=True, max_length=6, null=True)),
                ('last_login', models.DateTimeField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='staffregistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(blank=True, max_length=6, null=True)),
                ('firstname', models.TextField(blank=True, max_length=20, null=True)),
                ('lastname', models.TextField(blank=True, max_length=20, null=True)),
                ('date_of_birth', models.TextField(blank=True, max_length=10, null=True)),
                ('gender', models.TextField(blank=True, max_length=10, null=True)),
                ('contact_number', models.TextField(blank=True, max_length=10, null=True)),
                ('alternate_contact_number', models.TextField(blank=True, max_length=10, null=True)),
                ('email_id', models.TextField(blank=True, max_length=30, null=True)),
                ('residential_address', models.TextField(blank=True, max_length=100, null=True)),
                ('parmanent_address', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField(blank=True, max_length=20, null=True)),
                ('lastname', models.TextField(blank=True, max_length=20, null=True)),
                ('passport_number', models.CharField(blank=True, max_length=16, null=True)),
                ('mother_name', models.TextField(blank=True, max_length=20, null=True)),
                ('father_name', models.TextField(blank=True, max_length=20, null=True)),
                ('mother_passport_number', models.CharField(blank=True, max_length=16, null=True)),
                ('father_passport_number', models.CharField(blank=True, max_length=16, null=True)),
                ('date_of_birth', models.TextField(blank=True, max_length=10, null=True)),
                ('place_of_birth', models.TextField(blank=True, max_length=10, null=True)),
                ('residential_address', models.TextField(blank=True, max_length=100, null=True)),
                ('parmanent_address', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='stafflogin',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.staffregistration'),
        ),
        migrations.AddField(
            model_name='clientlogin',
            name='CLIENT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userdata'),
        ),
    ]
