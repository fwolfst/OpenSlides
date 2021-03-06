# Generated by Finn Stutzenstein on 2019-10-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assignments", "0009_voting_2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignmentvote",
            name="value",
            field=models.CharField(
                choices=[("Y", "Y"), ("N", "N"), ("A", "A")], max_length=1
            ),
        ),
        migrations.RemoveField(model_name="assignmentpoll", name="votesabstain"),
        migrations.RemoveField(model_name="assignmentpoll", name="votesno"),
        migrations.RemoveField(model_name="assignmentpoll", name="published"),
        migrations.RemoveField(model_name="assignmentrelateduser", name="elected"),
    ]
