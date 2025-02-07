# Generated by Django 4.0 on 2022-01-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_user_display_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="display_name",
            field=models.CharField(
                default="Given name",
                help_text="Helps other team members recognise you, such as by your given name or nickname.",
                max_length=15,
                verbose_name="display name",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
