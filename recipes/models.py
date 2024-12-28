from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('grams', 'Граммы'),
        ('kilograms', 'Килограммы'),
        ('milliliters', 'Миллилитры'),
        ('liters', 'Литры'),
        ('pieces', 'Штуки'),
    ]

    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    is_optional = models.BooleanField(default=False)
    calories = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.get_unit_display()})"


class Collection(models.Model):
    name = models.CharField(max_length=255)
    recipes = models.ManyToManyField(Recipe, related_name='collections')

    def __str__(self):
        return self.name
