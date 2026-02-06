from django.db import models
from django.core.exceptions import ValidationError


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название раздела'
    )

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    text = models.TextField(
        verbose_name='Текст статьи'
    )
    published_at = models.DateTimeField(
        verbose_name='Дата публикации'
    )
    image = models.ImageField(
        upload_to='articles/',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )

    scopes = models.ManyToManyField(
        Tag,
        through='ArticleScope',
        related_name='articles',
        verbose_name='Разделы',
        blank=True
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class ArticleScope(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='scopes'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='scopes'
    )
    is_main = models.BooleanField(
        default=False,
        verbose_name='Основной раздел'
    )

    class Meta:
        ordering = ['-is_main', 'tag__name']

    def __str__(self):
        return f"{self.article.title} - {self.tag.name}"

    def clean(self):
        if self.is_main and self.pk:
            other_main_scopes = ArticleScope.objects.filter(
                article=self.article,
                is_main=True
            ).exclude(pk=self.pk)

            if other_main_scopes.exists():
                raise ValidationError(
                    'У этой статьи уже есть основной раздел. '
                    'Основным может быть только один раздел.'
                )
