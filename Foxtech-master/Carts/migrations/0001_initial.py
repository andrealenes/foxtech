# Generated by Django 4.0.3 on 2022-11-20 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id_cart', models.AutoField(primary_key=True, serialize=False, verbose_name='Id carrito')),
                ('total', models.PositiveIntegerField(default=0, verbose_name='Total')),
                ('subtotal', models.PositiveIntegerField(default=0, verbose_name='Subtotal')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('identifier', models.CharField(max_length=100, unique=True, verbose_name='Identificador unico')),
            ],
            options={
                'verbose_name': 'Carrito de compras',
                'verbose_name_plural': 'Carritos de compras',
                'db_table': 'cart',
                'ordering': ['id_cart'],
            },
        ),
        migrations.CreateModel(
            name='CartProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Cantidad')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carts.cart', verbose_name='Carrito de compras')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product', verbose_name='Producto')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(through='Carts.CartProducts', to='Products.product'),
        ),
    ]
