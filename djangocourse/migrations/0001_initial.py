# Generated by Django 4.1.5 on 2023-01-29 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=250, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=250, verbose_name='Отчество')),
                ('email', models.CharField(max_length=250, verbose_name='Почта')),
                ('comment', models.CharField(max_length=250, verbose_name='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='DistributionMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=250, verbose_name='тема')),
                ('text', models.CharField(max_length=250, verbose_name='текст')),
            ],
        ),
        migrations.CreateModel(
            name='DistributionSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('periodicity', models.CharField(choices=[('day', 'день'), ('week', 'неделя'), ('month', 'месяц')], default='day', max_length=10, verbose_name='Период')),
                ('status', models.CharField(choices=[('created', 'создано'), ('launched', 'запущено'), ('completed', 'завершено')], default='created', max_length=10, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='DistributionTry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('success', 'успех'), ('fail', 'провал')], max_length=10, verbose_name='Статус')),
                ('server_return', models.CharField(choices=[('yes', 'да'), ('no', 'нет')], max_length=5, verbose_name='Ответ')),
            ],
        ),
    ]