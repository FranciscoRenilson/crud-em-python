from django.db import models

# Create your models here.


class Pizza(models.Model):  # cria a classe pizza
    description = models.CharField(max_length=100)  # variável descrição (caractere)
    price = models.DecimalField(max_digits=9, decimal_places=2)  # variável preço (número decimal)
    quantity = models.IntegerField()  # variável quantidade (inteira)

    objects = models.Manager()

    def __str__(self):
        return self.description
