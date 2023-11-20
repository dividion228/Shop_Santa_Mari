from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    """Категории, к которым относятся товары"""

    name = models.CharField(max_length=200, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """Товар входящий в разные категории"""

    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Выберите категорию')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Ниличие')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_rental = models.BooleanField(default=False, verbose_name='Прокат', db_index=True)
    price_is_rental = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена проката', blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, verbose_name='Фото')
    state_product = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Состояние')

    class Meta:
        ordering = ('name',)
        indexes = (models.Index(fields=('name', 'is_rental', 'id')))
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
