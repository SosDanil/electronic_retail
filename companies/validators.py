from rest_framework.serializers import ValidationError


class DontUpdateDebtValidator:
    """Не позволяет обновлять задолженность у компании"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val:
            raise ValidationError('Нельзя обновить задолженность перед поставщиком у объекта')


class WrongLevelValidator:
    """Проверяет, чтобы уровень иерархии был соответствующий при создании объекта сети"""

    def __init__(self, field1, field2, supplier):
        self.field1 = field1
        self.field2 = field2
        self.supplier = supplier

    def __call__(self, value):
        company_type = dict(value).get(self.field1)
        level = dict(value).get(self.field2)
        supplier = dict(value).get(self.supplier)
        if company_type == 'factory' and level != 'zero level':
            raise ValidationError('У завода должен быть нулевой уровень иерархии')
        elif company_type == 'store' and level == 'zero level' or company_type == 'SP' and level == 'zero level':
            raise ValidationError('У розничного магазина или ИП не может быть нулевой уровень иерархии')
        elif supplier is not None:
            if supplier.level == 'zero level' and level != 'first level':
                raise ValidationError('Укажите первый уровень иерархии')
            elif supplier.level == 'first level' and level != 'second level':
                raise ValidationError('Укажите второй уровень иерархии')
