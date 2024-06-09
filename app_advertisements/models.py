from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

User = get_user_model()


class ArticleScope(models.Model):
    scope = models.CharField("сфера деятельности", max_length=256)

    class Meta:
        verbose_name = "сфера деятельности"
        verbose_name_plural = "сферы деятельности"

    def __str__(self) -> str:
        return str(self.scope)


class HistoricalPerson(models.Model):
    full_name = models.CharField("полное имя", max_length=256)
    born_date = models.DateField(verbose_name="дата рождения")
    image = models.ImageField("изображение", upload_to="advertisements/")

    class Meta:
        verbose_name = "историческая персона"
        verbose_name_plural = "исторические персоны"

    def __str__(self) -> str:
        return str(self.full_name)


class Article(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        verbose_name='пользователь',
        on_delete=models.CASCADE,
        related_name="articles",
    )
    scope = models.ForeignKey(
        ArticleScope,
        verbose_name="сфера деятельности",
        on_delete=models.CASCADE,
        related_name="articles",
    )
    persons = models.ManyToManyField(
        HistoricalPerson,
        verbose_name="исторические персоны",
        related_name="articles",
    )
    is_published = models.BooleanField(
        verbose_name="опубликована",
        default=True
    )

    def get_absolute_url(self) -> str:
        return reverse('adv-detail', kwargs={'pk': self.pk})

    @admin.display(description='фото')
    def get_html_image(self):
        if self.images.first():
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"', url=self.images.first().image.url
            )

    def __str__(self) -> str:
        return f"({self.pk}). {self.title}"

    class Meta:
        verbose_name = "историческая статья"
        verbose_name_plural = "исторические статьи"


class ArticleImage(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("изображение", upload_to="advertisements/")
