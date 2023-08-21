from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    genders = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
        (None, 'Не указан')
    )

    name = models.CharField(max_length=30, unique=True, blank=False)
    gender = models.CharField(choices=genders, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.id}, name: {self.name}'


class City(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(blank=True, default='')
    coordinates = models.URLField(blank=True)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'


class Sight(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.TextField(blank=True)
    coordinates = models.URLField(blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    tourists = models.ManyToManyField(Author, through="AuthorSightRelation")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'


class Review(models.Model):
    text = models.TextField(blank=False)
    date = models.DateField(auto_now=True)
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)


class AuthorSightRelation(models.Model):
    rating_choices = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(choices=rating_choices, null=True)

    def __str__(self):
        return f'ID: {self.id}, author: {self.author.name}, sight: {self.sight.name}, rating: {self.rating}'

    def save(self, *args, **kwargs):
        from rating import set_rating

        creating = not self.pk
        old = self.rating
        super().save(*args, **kwargs)
        new = self.rating
        if old != new or creating:
            set_rating(self.sight)
