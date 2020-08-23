from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    image = models.ImageField(upload_to='images/items')
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    article = models.CharField(max_length=250)
    available = models.BooleanField()
    category = models.ForeignKey(Category,
                                 related_name='items',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
