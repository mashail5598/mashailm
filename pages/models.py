from django.db import models


class Slider(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="العنوان"
    )

    subtitle = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="الوصف المختصر"
    )

    image = models.ImageField(
        upload_to='sliders/',
        verbose_name="صورة السلايدر"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط"
    )

    class Meta:
        verbose_name = "سلايدر"
        verbose_name_plural = "السلايدر"

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="عنوان الصفحة"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="الرابط"
    )

    content = models.TextField(
        verbose_name="محتوى الصفحة"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    class Meta:
        verbose_name = "صفحة"
        verbose_name_plural = "الصفحات"

    def __str__(self):
        return self.title
