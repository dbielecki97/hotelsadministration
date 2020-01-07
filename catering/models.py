from django.db import models


class FoodQuantity(models.Model):
    foodItem = models.ForeignKey('Food', on_delete=models.CASCADE)
    catering = models.ForeignKey('Catering', on_delete=models.CASCADE)
    quantity = models.IntegerField('Ilość', null=False, blank=False, default=0)

    class Meta:
        verbose_name_plural = 'food quantities'

    def __str__(self):
        return '{} x{}'.format(self.foodItem.name, self.quantity)


class Catering(models.Model):
    foods = models.ManyToManyField('Food', through=FoodQuantity)

    def __str__(self):
        return 'Catering {}'.format(self.pk)


class Food(models.Model):
    name = models.CharField('Nazwa', max_length=50, blank=False, null=False)
    price = models.FloatField('Cena', blank=False, null=False)
    food_type = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Nazwa', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
