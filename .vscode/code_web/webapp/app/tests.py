from django.test import TestCase
from django.urls import reverse
from .models import Warehouse
from django.utils import timezone
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
class WarehouseModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        content_type = ContentType.objects.get_for_model(Warehouse)
        permission = Permission.objects.get(codename='view_warehouse', content_type=content_type)
        self.user.user_permissions.add(permission)
        self.client.login(username='testuser', password='password123')
        self.created_time = timezone.now()
        self.warehouse_item = Warehouse.objects.create(
            id_product="SP001",
            nameproduct="Chuột không dây",
            origin="Việt Nam",
            price=150000,
            instock=50,
            date_time=self.created_time,
            image="https://example.com/image.jpg"
        )

        print(Warehouse.objects.all())
    def test_str_method(self):
        self.assertEqual(str(self.warehouse_item), "SP001")
    def test_retrieve_product(self):
        # data = {
        #     "id_product"="SP001",
        #     "nameproduct"="Chuột không dây",
        #     "origin"="Việt Nam",
        #     "price"=150000,
        #     "instock"=50,
        #     "date_time"=self.created_time,
        #     "image"="https://example.com/image.jpg"
        # }
        url = reverse('warehouse_delete_api', kwargs={'id_product': self.warehouse_item.id_product})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id_product'], self.item.id_product)
        self.assertEqual(response.data['nameproduct'], self.item.nameproduct)