from django.core.management.base import BaseCommand
from shop.models import Category, Item
from django.db.models import Sum, Max, Min, Count

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        
        item_count = Category.objects.aggregate(item_count=Count('items'))
        print(item_count)
        item_count2 = Category.objects.annotate(item_count=Count('items'))
        item_sum = Category.objects.aggregate(item_count=Sum('items'))
        categorys = Item.objects.select_related('category').all()
        for category in categorys:
            print(category.name)
        tags = Item.objects.prefetch_related('tags').all()
        
