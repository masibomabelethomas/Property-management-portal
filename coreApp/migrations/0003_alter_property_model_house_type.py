# Generated by Django 4.2.2 on 2023-10-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0002_alter_property_model_house_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_model',
            name='house_type',
            field=models.PositiveIntegerField(choices=[('Singleroom', 'Singleroom'), ('Bedsitter', 'Bedsitter'), ('One bedroom', 'One bedroom'), ('Two bedroom', 'Two bedroom'), ('Three bedroom', 'Three bedroom'), ('Four bedroom', 'Four bedroom'), ('Studio', 'Studio'), ('Commercial shops', 'Commercial shops')]),
        ),
    ]
