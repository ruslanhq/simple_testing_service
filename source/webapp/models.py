from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=250, verbose_name='Описание', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', verbose_name='Тест', on_delete=models.CASCADE)
    text = models.TextField(max_length=250, verbose_name='Вопрос')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', verbose_name='Вопрос',
                                 on_delete=models.CASCADE)
    text = models.TextField(max_length=200, verbose_name='Ответ')
    is_valid = models.BooleanField(default=False, verbose_name='Верный ответ')

    def __str__(self):
        return '"{}" - {}'.format(self.text, 'valid' if self.is_valid else 'invalid')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

