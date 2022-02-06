from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Car(models.Model):
    mit = models.CharField(max_length=255, verbose_name='Mit', db_index=True)
    color = models.CharField(verbose_name='Color', max_length=60)
    mod = models.CharField(verbose_name='Model', max_length=200)
    image = models.ImageField(null=True, blank=True)
    CAR_TYPES = (
        (1, 'хэтчбек'),
        (2, 'Универсал'),
        (3, 'Седан'),
        (4, 'Внедорожник'),
    )
    car_type = models.IntegerField(verbose_name='Car_type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.mit