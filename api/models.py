from django.db import models


class Breed(models.Model):
    TINY = 'Tiny'
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'

    SIZE_CHOICES = (
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    )

    LEVEL = [
        (1, '1 - min'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 - max'),
    ]

    name_of_breed = models.CharField(max_length=46, verbose_name='Название породы')
    size = models.CharField(
        max_length=6,
        choices=SIZE_CHOICES,
        default=MEDIUM,
    )
    friendliness = models.IntegerField(
        choices=LEVEL,
        default=3,
        help_text='Уровень дружелюбности от 1 (Минимально дружелюбный) до 5 (Максимально дружелюбный).',
        verbose_name='Дружелюбность'
    )
    trainability = models.IntegerField(
        choices=LEVEL,
        default=3,
        help_text='Уровень обучаемости от 1 (не обучаемый) до 5 (легкообучаемый)',
        verbose_name='Обучаемость'
    )
    shedding_amount = models.IntegerField(
        choices=LEVEL,
        default=3,
        help_text='Уровень линьки шерсти от 1 (не линяет) до 5 (все вокруг в шерсти)',
        verbose_name='Уровень линьки'

    )
    exercise_needs = models.IntegerField(
        choices=LEVEL,
        default=3,
        help_text='Уровень необходимых тренировок от 1 (тренировки необязательны) до 5 (необходимы постоянно)',
        verbose_name='Уровень необходимых тренировок'

    )

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
        ordering = ['size']
        db_table = 'breeds'

    def __str__(self):
        return self.name_of_breed


class Dog(models.Model):
    name = models.CharField(max_length=46, verbose_name='Имя собаки')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    breed = models.ForeignKey(Breed,
                              on_delete=models.CASCADE,
                              related_name='dog')
    gender = models.CharField(max_length=20, verbose_name='Гендер')
    color = models.CharField(max_length=25, verbose_name='Цвет')
    favorite_food = models.CharField(max_length=80, verbose_name='Любимая еда')
    favorite_toy = models.CharField(max_length=52, verbose_name='Любимая игрушка')

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
        ordering = ['age']
        db_table = 'dogs'

    def __str__(self):
        return self.name
