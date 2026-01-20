from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    نموذج مستخدم مخصص
    """

    email = models.EmailField(
        unique=True,
        verbose_name="البريد الإلكتروني"
    )

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمون"

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name="المستخدم"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="رقم الجوال"
    )

    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name="الصورة الشخصية"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    class Meta:
        verbose_name = "الملف الشخصي"
        verbose_name_plural = "الملفات الشخصية"

    def __str__(self):
        return self.user.username


class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name="المستخدم"
    )

    city = models.CharField(
        max_length=100,
        verbose_name="المدينة"
    )

    district = models.CharField(
        max_length=100,
        verbose_name="الحي"
    )

    street = models.CharField(
        max_length=200,
        verbose_name="الشارع"
    )

    notes = models.TextField(
        blank=True,
        verbose_name="ملاحظات إضافية"
    )

    class Meta:
        verbose_name = "عنوان"
        verbose_name_plural = "العناوين"

    def __str__(self):
        return f"{self.city} - {self.district}"
