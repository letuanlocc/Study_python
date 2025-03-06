from django.db import models
# Create your models here.
class Products(models.Model):
    product_id = models.AutoField(primary_key=True, db_column="ProductID")
    product_name = models.CharField(max_length=40, db_column="ProductName")
    supplier_id = models.IntegerField(null=True, blank=True, db_column="SupplierID")
    category_id = models.IntegerField(null=True, blank=True, db_column="CategoryID")
    quantity_per_unit = models.CharField(max_length=20, null=True, blank=True, db_column="QuantityPerUnit")
    unit_price = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True, db_column="UnitPrice")
    class Meta:
        db_table = "Products"  # Giữ nguyên tên bảng trong database
    def __str__(self):
        return f"{self.product_id} - {self.product_name} - {self.supplier_id} - {self.category_id}"