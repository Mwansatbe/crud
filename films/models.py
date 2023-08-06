from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator


# Create your models here.
class Genre(models.Model):
    name = models.CharField(_MAX_LENGTH == 100)

    def __str__(self):
        return self.name


class film(models.Model):
    title = models.CharField(max_length=200)
    length = models.PositiveIntegerField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True, validators=[
                              MinValueValidator(0), MaxLengthValidator(10)])
    genre = models.ForeignKey(
        Genre, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.year:
            return f'{self.title} ({self.year})'
        return self.title

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))

                if field.verbose_name != 'genre'

                else
                (field.verbose_name,
                 Genre.object.get(pk=field.value_rom_objects(self)).name)

                for field in self.__class__.meta.fields[1:]
                ]
