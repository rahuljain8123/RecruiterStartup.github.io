# Generated by Django 4.2.3 on 2023-08-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiter', '0008_alter_job_contact_email_alter_job_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='description',
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Temporary', 'Temporary'), ('Full-Time', 'Full-Time'), ('Contract', 'Contract'), ('Part-Time', 'Part-Time')], max_length=50),
        ),
    ]
