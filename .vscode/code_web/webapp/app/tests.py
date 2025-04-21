from django.test import TestCase
from django.urls import reverse
from .models import Warehouse
from django.utils import timezone
class WarehouseModelTestCase(TestCase):
    def setUp(self):
        self.created_time = timezone.now()
        # Tạo dữ liệu mẫu cho model Warehouse
        self.warehouse_item = Warehouse.objects.create(
            id_product="SP001",
            nameproduct="Chuột không dây",
            origin="Việt Nam",
            price=150000,
            instock=50,
            date_time=self.created_time,
            image="https://example.com/image.jpg"
        )

    def test_warehouse_creation(self):
        self.assertEqual(self.warehouse_item.id_product, "SP001")
        self.assertEqual(self.warehouse_item.nameproduct, "Chuột không dây")
        self.assertEqual(self.warehouse_item.origin, "Việt Nam")
        self.assertEqual(self.warehouse_item.price, 150000)
        self.assertEqual(self.warehouse_item.instock, 50)
        self.assertEqual(self.warehouse_item.date_time,self.created_time)
        self.assertEqual(self.warehouse_item.image,)
        self.assertEqual(self.warehouse_item.image, "https://example.com/image.jpg")

    def test_warehouse_update(self):
        """Kiểm tra cập nhật thông tin sản phẩm"""
        self.warehouse_item.price = 200000
        self.warehouse_item.instock = 30
        self.warehouse_item.save()

        updated_item = Warehouse.objects.get(id_product="SP001")
        self.assertEqual(updated_item.price, 200000)
        self.assertEqual(updated_item.instock, 30)

    def test_warehouse_delete(self):
        """Kiểm tra xóa sản phẩm"""
        self.warehouse_item.delete()
        self.assertEqual(Warehouse.objects.count(), 0)

