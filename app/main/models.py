# bakery/models.py

from django.db import models

class Pao(models.Model):
    quantidade_feita = models.IntegerField(default=0)
    quantidade_vendida = models.IntegerField(default=0)
    preco_unitario = models.DecimalField(max_digits=5, decimal_places=2, default=0.40)


class Sale(models.Model):
    customer_name = models.CharField(max_length=100)
    quantity_sold = models.IntegerField(default=0)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.customer_name} comprou {self.quantity_sold} pães'
