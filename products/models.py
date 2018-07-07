from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'product'


class Warehouse(models.Model):
    id = models.AutoField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'warehouse'


class Warehouse_statement(models.Model):
    id = models.AutoField(primary_key=True, max_length=20)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING)
    enter = models.IntegerField(max_length=2)
    amount = models.IntegerField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'warehouse_statement'
