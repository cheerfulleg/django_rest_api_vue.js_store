from rest_framework import serializers

from .models import Item, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Item
        fields = ('image', 'name', 'price', 'article', 'available', 'category',)

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(name=category_data)
        item = Item.objects.create(category=category, **validated_data)
        return item
