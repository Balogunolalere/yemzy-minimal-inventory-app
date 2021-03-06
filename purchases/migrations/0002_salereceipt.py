# Generated by Django 4.0.4 on 2022-06-06 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField(auto_now_add=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_quantity', models.IntegerField(default=1)),
                ('total_amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sales_rep', models.CharField(max_length=200)),
                ('item_description', models.TextField(blank=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.salebill')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.customer')),
            ],
            options={
                'ordering': ['-bill_date'],
            },
        ),
    ]
