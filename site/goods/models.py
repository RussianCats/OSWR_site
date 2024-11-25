from unicodedata import category
from django.db import models
from numpy import quantile

# Create your models here.
class Categories(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True,
        verbose_name="Категория"
        )
    # текстовый адрес ввести на категорию
    slug = models.SlugField(
        max_length=200, 
        unique=True, 
        blank=True, 
        null=True,
        verbose_name="Ссылка (URL)"
        ) 
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True,
        verbose_name="Название"
        )
    slug = models.SlugField(
        max_length=200, 
        unique=True, 
        blank=True, 
        null=True,
        verbose_name="Ссылка (URL)"
        ) 
    description = models.TextField(
        blank=True, 
        null=True,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='goods_images',
        blank=True, 
        null=True,
        verbose_name="Изображение"
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name="Цена"
    )
    discout = models.DecimalField(
        default=0.00,
        max_digits=4,
        decimal_places=2,
        verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество"
    )
    category = models.ForeignKey(
        to=Categories,
        on_delete=models.PROTECT,
        verbose_name="Категория"
    )

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural: str = 'Продукты'

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}' 


