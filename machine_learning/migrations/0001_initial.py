# Generated by Django 3.2.13 on 2023-11-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MLModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('trained_on', models.DateField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='PredictedContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ml_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine_learning.mlmodel')),
            ],
        ),
    ]
