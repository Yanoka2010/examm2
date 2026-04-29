from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class Category(models.Model):
    """Раздел каталога книг (жанр, учебная дисциплина и т.п.)"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Название раздела")

    class Meta:
        verbose_name = "Раздел каталога"
        verbose_name_plural = "Разделы каталога"
        ordering = ['name']

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    """Издательство"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Название издательства")

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"
        ordering = ['name']

    def __str__(self):
        return self.name


class Supplier(models.Model):
    """Поставщик книг (оптовик, дистрибьютор)"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Название поставщика")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ['name']

    def __str__(self):
        return self.name


class Unit(models.Model):
    """Единица измерения"""
    name = models.CharField(max_length=50, unique=True, verbose_name="Единица измерения")
    abbreviation = models.CharField(max_length=10, blank=True, verbose_name="Сокращение")

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Книга в каталоге"""
    name = models.CharField(max_length=200, verbose_name="Название книги")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Раздел каталога")
    description = models.TextField(blank=True, verbose_name="Аннотация")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Издательство")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Поставщик")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Цена"
    )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="Единица измерения")
    quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Остаток на складе (экз.)"
    )
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('100.00'))],
        verbose_name="Скидка (%)"
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name="Обложка"
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def final_price(self):
        """Расчетная цена с учетом скидки"""
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    @property
    def is_available(self):
        """Проверка наличия книги на складе"""
        return self.quantity > 0
