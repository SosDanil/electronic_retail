from rest_framework.serializers import ValidationError


class DontUpdateDebtValidator:
    """Не позволяет обновлять задолженность у компании"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val:
            raise ValidationError('Нельзя обновить задолженность перед поставщиком у объекта')
