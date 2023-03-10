# Generated by Django 4.0 on 2022-12-17 11:20

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Details',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=500)),
                ('book_image', models.FileField(upload_to='./static/images')),
                ('book_desc', models.FileField(upload_to='./static/books')),
            ],
        ),
    ]
