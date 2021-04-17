from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='media/category/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    SIZE_PRODUCT = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    FOR_WHOM = (
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Child', 'Child')
    )
    owner = models.ForeignKey(User, related_name='product_created', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media/products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    sold = models.BooleanField(default=False)
    payments = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    bought_by = models.ForeignKey(User, related_name='bought_by', on_delete=models.CASCADE)
    size = models.CharField(max_length=15, choices=SIZE_PRODUCT)
    for_whom = models.CharField(max_length=15, choices=FOR_WHOM)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(User, related_name='message_created', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='message_recipentd', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField(blank=True)
    send = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.title
