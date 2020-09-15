import base64

from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=30,
        unique=True
    )
    subcategories = models.ManyToManyField(
        'self',
        blank=True,
    )
    slug = models.SlugField()


class Brend(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True
    )
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Model(models.Model):
    title = models.CharField(max_length=50)
    categories = models.ManyToManyField(
        'avto.Category',
        blank=True
    )

    def __str__(self):
        return self.title


class ModelImage(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='models/%Y/%m/%d/')
    image_base64 = models.TextField(default=None, null=True, blank=True)
    model = models.ForeignKey(
        'avto.Model',
        related_name='images_model',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if self.image:
            self.image_base64 = 'data:{content_type};base64,{data}'.format(
                content_type='jpeg',
                data=base64.b64encode(
                    self.image.file.read()
                ).decode()
            )
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        return self.image_base64 or self.image.url


class Generation(models.Model):
    title = models.CharField(max_length=50)
    year_begin = models.PositiveIntegerField()
    year_end = models.PositiveIntegerField()
    models = models.ManyToManyField(Model)

    def __str__(self):
        return self.title

class Characteristic(models.Model):

    class EngineVolume(models.IntegerChoices):
        EIGHT_HUNDRED = 800
        NINE_HUNDRED = 900
        ONE_THOUSAND = 1000
        ELEVEN_HUNDRED = 1100
        TWELWE_HUNDRED = 1200
        THIRTING_HUNDRED = 1300


    class Fuel(models.TextChoices):
        NATURAL_GAS = 'Natural Gas', 'Газ'
        GASOLINE = 'Gasoline', 'Бензин'
        HYBRID = 'Gasoline Hybrid', 'Гибрид'
        DIESEL = 'Diesel', 'Дизель'
        ELECTRIC = 'Electric', 'Электро'

    class BodyType(models.TextChoices):
        CARGO_VAN = 'Cargo Van', 'Грузовой фургон'
        CONVERTIBLE = 'Convertible', 'Кабриолет'
        COUPE = 'Coupe', 'Купе'
        HATCHBACK = 'Hatchback', 'Хетчбэк'
        LIMOUSINE = 'Limousine', 'Лимузин'
        MINIVAN = 'Minivan', 'Минивэн'
        PASSENGER_VAN = 'Passenger Van', 'Микроавтобус'
        PICKUP = 'Pickup', 'Пикап'
        SEDAN = 'Sedan', 'Седан'
        SUV = 'SUV', 'Внедорожник'
        WAGON = 'Wagon', 'Универсал'

    class Gearbox(models.TextChoices):
        MANUAL = 'Manual', ' Механическая'
        AUTOMATIC = 'Automatic', 'Автоматическая'

    class Drivetrain(models.TextChoices):
        AWD = 'AWD', 'Полный привод'
        FWD = 'FWD', 'Передний привод'
        RWD = 'RWD', 'Задний привод'

    class Door(models.IntegerChoices):
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6

    class Seat(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        ELEVEN = 11
        TWELWE = 12

    engine_volue = models.IntegerField(
        choices=EngineVolume.choices,
        default=EngineVolume.THIRTING_HUNDRED,
        verbose_name='Объем двигателя'
    )
    flue = models.CharField(
        max_length=15,
        choices=Fuel.choices,
        default=Fuel.GASOLINE,
        verbose_name='Вид топлива'
    )
    body_type = models.CharField(
        max_length=15,
        choices=BodyType.choices,
        default=BodyType.SEDAN,
        verbose_name='Тип кузова'
    )
    gearbox = models.CharField(
        max_length=15,
        choices=Gearbox.choices,
        default=Gearbox.AUTOMATIC,
        verbose_name='Коробка передач'
    )
    drivetrain = models.CharField(
        max_length=17,
        choices=Drivetrain.choices,
        default=Drivetrain.FWD,
        verbose_name='Привод'
    )
    door = models.CharField(
        max_length=1,
        choices=Door.choices,
        default=Door.FOUR,
        verbose_name='Количество дверей'
    )
    seat = models.CharField(
        max_length=2,
        choices=Seat.choices,
        default=Seat.FIVE,
        verbose_name='Количество мест'
    )
    mileage = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Пробег'
    )
    models = models.ForeignKey(
        'avto.Model',
        on_delete=models.CASCADE,
        related_name='Characteristic'
    )
