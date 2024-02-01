# Generated by Django 4.2.5 on 2023-09-25 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookstoredb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=500)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image_url', models.CharField(max_length=5000)),
                ('Book_availability', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('items', models.ManyToManyField(to='app2.bookstoredb')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cartitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.bookstoredb')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.cart')),
            ],
        ),
    ]