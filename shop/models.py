from django.db import models
import uuid
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(default='', unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # Used to create a URL name for a category instead of UUID
    # https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    # --------------------------------------- 

    def get_absolute_url(self):
        return reverse('shop:products_by_category', args=[self.slug])

    def __str__(self):
        return self.name
    
class ControlMechanism(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='control_mechanism', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'control mechanism'
        verbose_name_plural = 'control mechanisms'

    def get_absolute_url(self):
        return reverse('shop:products_by_control_mechanism', args=[self.id])

    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    country = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def get_absolute_url(self):
        return reverse('shop:products_by_brand', args=[self.id])

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=250, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    control_mechanism = models.ForeignKey(ControlMechanism, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to = 'product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank = True, null= True)
    updated = models.DateTimeField(auto_now=True, blank = True, null= True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.category.id, self.id])

    def __str__(self):
        return self.name