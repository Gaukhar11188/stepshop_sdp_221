from django.db import models

from stepshop import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        verbose_name="Количество",
        default=0,
    )

    add_datetime = models.DateTimeField(
        verbose_name="Время",
        auto_now_add=True,
    )

