from django.db import models

#если поле необязательно для заполнения
NULLABLE = {'blank': True, 'null': True}

class Student(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    email = models.EmailField(max_length=150, unique=True, verbose_name='почта', **NULLABLE)

    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)
    #в указанную папку будет складываться вся метаинформация из модели
    is_active = models.BooleanField(default=True, verbose_name='активный')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='студент')

    def __str__(self):
        return f'{self.title} ({self.student})'

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'