# Generated by Django 5.1 on 2024-09-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_alter_company_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='level',
            field=models.CharField(choices=[('zero level', 'нулевой уровень'), ('first level', 'первый уровень'), ('second level', 'второй уровень')], max_length=50, verbose_name='уровень иерархии'),
        ),
    ]
