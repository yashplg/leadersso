# Generated by Django 4.1.3 on 2022-11-14 09:23
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_policies_password", "0004_passwordpolicy_authentik_p_policy__855e80_idx"),
    ]

    operations = [
        migrations.AddField(
            model_name="passwordpolicy",
            name="check_have_i_been_pwned",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="passwordpolicy",
            name="check_static_rules",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="passwordpolicy",
            name="check_zxcvbn",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="passwordpolicy",
            name="hibp_allowed_count",
            field=models.PositiveIntegerField(
                default=0,
                help_text="How many times the password hash is allowed to be on haveibeenpwned",
            ),
        ),
        migrations.AddField(
            model_name="passwordpolicy",
            name="zxcvbn_score_threshold",
            field=models.PositiveIntegerField(
                default=2,
                help_text="If the zxcvbn score is equal or less than this value, the policy will fail.",
            ),
        ),
        migrations.AlterField(
            model_name="passwordpolicy",
            name="error_message",
            field=models.TextField(blank=True),
        ),
    ]
