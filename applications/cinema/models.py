from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


"""
Делаем модельку поста
"""
class Movie(models.Model):
    ### Owner - свзяываем с нашим юзером
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Владелец')
    ### title - даем название
    title = models.CharField('Название', max_length=50,)
    ### description - одаем описание к модельке
    description = models.TextField('Описание', blank=True, null=True)
    ### создаем дату создания , дату обнавления
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    update_at = models.DateTimeField('Дата обнавления', auto_now=True)
    ### переопределяем str для вывода title
    def __str__(self):
        return f'{self.title}'


class Like(models.Model):
    ### owner - свзязываем c нашим  user
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    ### movie - свзязываем с нашей моделькой фильмов Movie, мы можем обращаться к нашим связанным объектам через 'likes'
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')
    ### is_like по умолчанию  False
    is_like = models.BooleanField(default=False)
    ### переопределяем метод str
    def __str__(self):
        return f'{self.owner} --> {self.movie.title}'


class Rating(models.Model):
    ### owner - свзязываем c нашим  user
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    ### movie - свзязываем с нашей моделькой фильмов Movie, мы можем обращаться к нашим связанным объектам через 'likes'
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    """
    PositiveSmallIntegerField - предназначен для хранения целых чисел в диапазоне от 0 до 32767 
    Он гарантирует, что значение в поле будет неотрицательным и в пределах указанного диапазона.
    он удобен тем что экономит наши ресурсы 
    """
    ### validators используется для определения функций проверки
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5),
    ], blank=True, null=True)

    def __str__(self):
        return f'{self.owner} --> {self.movie.title}'







