from django.urls import reverse
from django.test import TestCase

from sale.models import Client, Supplier, Category, Product, Delivery, DeliveryItem, Sale, SaleItem

# Create your tests here.
class TestSaleViews(TestCase):
    def test_homeview(self):
        url = reverse('sale:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestSaleModels(TestCase):
    def create_category(self):
        return Category.objects.create(name='T-shirt')

    def create_product(self):
        c = self.create_category()
        p = Product.objects.create(
            code='101',
            name='Sport T-shirt',
            category=c,
            value=20000,
            image_link='-'
        )
        return p

    def create_delivery(self):
        return Delivery.objects.create()

    def create_sale(self):
        return Sale.objects.create()

    def test_client(self):
        client = Client.objects.create(name='Batman', contact='Gotham')
        self.assertIsInstance(client, Client)
        self.assertEqual(client.__str__(), client.name)

    def test_supplier(self):
        s = Supplier.objects.create(name='Alfred', contact='Gotham', payment_method='None')
        self.assertIsInstance(s, Supplier)
        self.assertEqual(s.__str__(), s.name)

    def test_category(self):
        c = self.create_category()
        self.assertIsInstance(c, Category)
        self.assertEqual(c.__str__(), c.name)

    def test_product(self):
        p = self.create_product()
        self.assertIsInstance(p, Product)
        self.assertEqual(p.__str__(), '{}-{}'.format(p.code, p.name))

    def test_delivery(self):
        d = self.create_delivery()
        self.assertIsInstance(d, Delivery)
        self.assertEqual(d.__str__(), '({})-{}'.format(d.id, d.creation_date))

    def test_delivery_item(self):
        d = self.create_delivery()
        di = DeliveryItem.objects.create(item=1, sell_value=20000, percentage=30, delivery=d)
        self.assertIsInstance(di, DeliveryItem)
        self.assertEqual(di.__str__(), '{} - {}'.format(di.delivery, di.item))

    def test_sale(self):
        s = self.create_sale()
        self.assertIsInstance(s, Sale)
        self.assertEqual(s.__str__(), '({})-{}'.format(s.id, s.creation_date))


    def test_sale_item(self):
        s = self.create_sale()
        si = SaleItem.objects.create(value=20000, expense=0, expense_description='', sale=s)
        self.assertIsInstance(si, SaleItem)
        self.assertEqual(si.__str__(), '{} - {}'.format(si.sale, si.id))