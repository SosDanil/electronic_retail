from django.db import models


class Company(models.Model):
    """Класс для завода, розничного магазина, ИП"""

    FACTORY = 'factory'
    STORE = 'store'
    SOLE_PROPRIETOR = 'SP'

    COMPANY_TYPE = (
        (FACTORY, 'Завод'),
        (STORE, 'розничный магазин'),
        (SOLE_PROPRIETOR, 'ИП'),
    )

    ZERO_LEVEL = 0
    FIRST_LEVEL = 1
    SECOND_LEVEL = 2

    LEVELS = (
        (ZERO_LEVEL, 'нулевой уровень иерархии'),
        (FIRST_LEVEL, 'первый уровень иерархии'),
        (SECOND_LEVEL, 'второй уровень иерархии'),
    )

    name = models.CharField(max_length=300, verbose_name='название')
    email = models.EmailField(verbose_name='почта', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='страна', blank=True, null=True)
    city = models.CharField(max_length=150, verbose_name='страна', blank=True, null=True)
    street = models.CharField(max_length=200, verbose_name='страна', blank=True, null=True)
    house_number = models.PositiveSmallIntegerField(verbose_name='номер дома',  blank=True, null=True)

    type = models.CharField(max_length=50, verbose_name='тип компании', choices=COMPANY_TYPE)
    level = models.CharField(max_length=10, verbose_name='уровень иерархии', choices=LEVELS)

    supplier = models.ForeignKey('self', verbose_name='поставщик', blank=True, null=True, on_delete=models.SET_NULL)
    debt = models.DecimalField(decimal_places=2, max_digits=100, verbose_name='долг перед поставщиком (в рублях)',
                               blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f"{self.name} ({self.country}, {self.city})"

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'


class Product(models.Model):
    """Класс для продукта, производимого какой-либо компанией"""

    name = models.CharField(max_length=400, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель продукта', blank=True, null=True)
    release_date = models.DateField(verbose_name='дата выхода на рынок', blank=True, null=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='компания')

    def __str__(self):
        return f"{self.name} от компании {self.company}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
