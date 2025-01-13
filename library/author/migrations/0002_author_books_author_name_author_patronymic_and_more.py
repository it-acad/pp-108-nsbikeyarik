# Generated by Django 4.1 on 2022-08-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(0, 'visitor'), (1, 'admin')], default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(default=None, max_length=255),
        ),
    ]

# # Generated by Django 4.1 on 2022-08-28 20:06
#
# from django.db import migrations, models
#
#
# class Migration(migrations.Migration):
#     dependencies = [
#         ('book', '0002_book_count_book_description_book_name_alter_book_id'),
#         ('author', '0001_initial'),
#     ]
#
#     operations = [
#         migrations.AddField(
#             model_name='authors',
#             name='books',
#             field=models.ManyToManyField(related_name='authors', to='book.book'),
#         ),
#         migrations.AddField(
#             model_name='authors',
#             name='name',
#             field=models.CharField(blank=True, max_length=20),
#         ),
#         migrations.AddField(
#             model_name='authors',
#             name='patronymic',
#             field=models.CharField(blank=True, max_length=20),
#         ),
#         migrations.AddField(
#             model_name='authors',
#             name='surname',
#             field=models.CharField(blank=True, max_length=20),
#         ),
#         migrations.AlterField(
#             model_name='authors',
#             name='id',
#             field=models.AutoField(primary_key=True, serialize=False),
#         ),
#     ]