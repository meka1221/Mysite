from django.db import models
from django.core.validators import MinValueValidator


class Marka(models.Model):
    title_marka = models.CharField(max_length=100)

    def __str__(self):
        return self.title_marka


class Model(models.Model):
    title_model = models.CharField(max_length=100)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_model


class Category(models.Model):
    title_category = models.CharField(max_length=100)

    def __str__(self):
        return self.title_category


class Car(models.Model):
    title_car = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField(default=0)
    year = models.DateTimeField(verbose_name='Год выпуска', auto_now_add=True)
    mileage = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    with_photo = models.BooleanField()
    CHOICES_COLOR = (
        ("черный ", "черный "),
        ("красный", "красный"),
        ("голубой", "голубой"),
        ("серый", "серый"),
        ("белый", "белый"),
    )
    color = models.CharField(verbose_name='Цвет', max_length=16, choices=CHOICES_COLOR)
    volume = models.FloatField(validators=[MinValueValidator(0)])
    CHOICES_BOX = (
        ('Автомат','Автомат'),
        ('Механика','Механика')
    )
    box = models.CharField(verbose_name='Коробка', max_length=16, choices=CHOICES_BOX)
    CHOICES_DRIVE = (
        ("Задний", "Задний"),
        ("Передний", "Передний"),
        ("Полный привод", "Полный привод"),
    )
    drive = models.CharField(verbose_name='Привод', max_length=16, choices=CHOICES_DRIVE)
    description = models.TextField()

    def __str__(self):
        return self.title_car


class CarPhoto(models.Model):
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


class Bet(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    total_number = models.IntegerField(default=0)
    buy_now = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title_bet
