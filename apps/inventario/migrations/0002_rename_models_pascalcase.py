from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventario", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="clave",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
