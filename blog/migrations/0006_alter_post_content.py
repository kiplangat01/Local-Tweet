# Generated by Django 4.0.4 on 2022-06-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ImageField(upload_to=''),
        ),
    ]
