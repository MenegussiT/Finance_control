# Generated by Django 5.1.2 on 2024-10-20 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_rename_revenue_category_expensecategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.expensecategory'),
        ),
    ]
