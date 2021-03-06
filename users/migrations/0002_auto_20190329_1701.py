# Generated by Django 2.1.7 on 2019-03-29 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='accomodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.TextField(blank=True, max_length=6, null=True)),
                ('file_upload', models.ImageField(blank=True, null=True, upload_to='accomodation/')),
            ],
        ),
        migrations.CreateModel(
            name='customersupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=20, null=True)),
                ('email', models.TextField(blank=True, max_length=30, null=True)),
                ('message', models.TextField(blank=True, max_length=300, null=True)),
                ('status', models.TextField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=20, null=True)),
                ('email', models.TextField(blank=True, max_length=30, null=True)),
                ('comment', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.TextField(blank=True, max_length=6, null=True)),
                ('cheque_number', models.TextField(blank=True, max_length=30, null=True)),
                ('bank_name', models.TextField(blank=True, max_length=30, null=True)),
                ('branch_name', models.TextField(blank=True, max_length=30, null=True)),
                ('net_amount', models.TextField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pnrstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.CharField(blank=True, max_length=6, null=True)),
                ('pnrno', models.CharField(blank=True, max_length=8, null=True)),
                ('ticket_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='visadetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.CharField(blank=True, max_length=6, null=True)),
                ('application_number', models.CharField(blank=True, max_length=14, null=True)),
                ('file_upload', models.ImageField(blank=True, null=True, upload_to='visa/')),
            ],
        ),
        migrations.RenameField(
            model_name='staffregistration',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='staffregistration',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='staffregistration',
            old_name='parmanent_address',
            new_name='permanent_address',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='parmanent_address',
            new_name='permanent_address',
        ),
        migrations.RemoveField(
            model_name='clientlogin',
            name='CLIENT',
        ),
        migrations.RemoveField(
            model_name='stafflogin',
            name='staff',
        ),
        migrations.AddField(
            model_name='modification',
            name='date',
            field=models.DateTimeField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='alternate_phone_number',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='batch_number',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='email',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='file_upload',
            field=models.ImageField(blank=True, null=True, upload_to='passports/'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='gender',
            field=models.TextField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='phone_number',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='clientlogin',
            name='last_login',
            field=models.DateTimeField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='stafflogin',
            name='last_login',
            field=models.DateTimeField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staffregistration',
            name='gender',
            field=models.TextField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='father_name',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='father_passport_number',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='mother_name',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='mother_passport_number',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='passport_number',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='place_of_birth',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
