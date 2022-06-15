from django.test import TestCase
from .models import Item


# Create your tests here.
class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name = 'Test To Do Item')
        self.assertFalse(item.done)

    def test_item_strings_method_returns_name(self):
        item = Item.objects.create(name = 'Test To Do Item')
        self.assertEqual(str(item), 'Test To Do Item')
