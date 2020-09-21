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
    slug = models.SlugField(verbose_name='Слаг')
    description = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Brend(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True
    )
    country = models.CharField(max_length=50)
    description = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.title


class Model(models.Model):
    title = models.CharField(max_length=50)
    categories = models.ManyToManyField(
        'avto.Category',
        blank=True
    )
    brends = models.ForeignKey(
        'avto.Brend',
        on_delete=models.CASCADE,
        related_name='models'
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.title


class ModelImage(models.Model):
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='generations/%Y/%m/%d/')
    image_base64 = models.TextField(default=None, null=True, blank=True)
    model = models.ForeignKey(
        'avto.Generation',
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

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Generation(models.Model):
    title = models.CharField(max_length=50)
    year_begin = models.PositiveIntegerField()
    year_end = models.PositiveIntegerField()
    models = models.ManyToManyField('avto.Model')


    class Meta:
        verbose_name = 'Поколение'
        verbose_name_plural = 'Поколения'

    def __str__(self):
        return self.title

class Equipment(models.Model):

    class EngineVolume(models.IntegerChoices):
        EIGHT_HUNDRED = 800
        NINE_HUNDRED = 900
        ONE_THOUSAND = 1000
        ELEVEN_HUNDRED = 1100
        TWELWE_HUNDRED = 1200
        THIRTING_HUNDRED = 1300
        FOURTEEN_HUNDRED = 1400
        FIFTEEN_HUNDRED = 1500
        SIXTEEN_HUNDRED = 1600
        SEVENTEEN_HUNDRED = 1700
        EIGHTEEN_HUNDRED = 1800
        NINETEEN_HUNDRED = 1900
        TWENTY_HUNDRED = 2000
        TWENTY_ONE_HUNDRED = 2100
        TWENTY_TWO_HUNDRED = 2200
        TWENTY_THREE_HUNDRED = 2300
        TWENTY_FOUR_HUNDRED = 2400
        TWENTY_FIVE_HUNDRED = 2500
        TWENTY_SIX_HUNDRED = 2600
        TWENTY_SEVEN_HUNDRED = 2700
        TWENTY_EIGHT_HUNDRED = 2800
        TWENTY_NINE_HUNDRED = 2900
        THIRTY_HUNDRED = 3000
        THIRTY_ONE_HUNDRED = 3100
        THIRTY_TWO_HUNDRED = 3200
        THIRTY_FIVE_HUNDRED = 3500
        THIRTY_SIX_HUNDRED = 3600
        FOURTY_HUNDRED = 4000
        FOURTY_FIVE_HUNDRED = 4500
        FIFTY_HUNDRED = 5000
        FIFTY_FIVE_HUNDRED = 5500
        SIXTY_HUNDRED = 6000
        SEVENTY_HUNDRED = 7000
        EIGHTY_HUNDRED = 8000

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
        ROBOTIC = 'Robotic', 'Робот'

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

    title = models.CharField(
        max_length=30,
    )
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
    door = models.IntegerField(
        choices=Door.choices,
        default=Door.FOUR,
        verbose_name='Количество дверей'
    )
    seat = models.IntegerField(
        choices=Seat.choices,
        default=Seat.FIVE,
        verbose_name='Количество мест'
    )
    mileage = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Пробег'
    )
    consumption_city = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Расход город'
    )
    consumption_road= models.FloatField(
        null=True,
        blank=True,
        verbose_name='Расход трасса'
    )
    acceleration = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Разгон'
    )
    capacity = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Мощность'
    )
    generations = models.ForeignKey(
        'avto.Generation',
        on_delete=models.CASCADE,
        related_name='Characteristic',
        verbose_name='Поколение'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектации'