from django.db import models
from cloudinary.models import CloudinaryField


# ==================================================
# التصنيفات
# ==================================================
class Category(models.Model):

    name = models.CharField(
        max_length=150,
        verbose_name="اسم التصنيف"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="الرابط"
    )

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


# ==================================================
# المنتجات
# ==================================================
class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="التصنيف"
    )

    name = models.CharField(
        max_length=200,
        verbose_name="اسم المنتج"
    )

    description = models.TextField(
        verbose_name="وصف المنتج"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )

    # ✅ صورة رئيسية (Cloudinary)
    image = CloudinaryField(
        verbose_name="الصورة الرئيسية",
        folder="products"
    )

    is_available = models.BooleanField(
        default=True,
        verbose_name="متوفر للبيع"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name


# ==================================================
# صور إضافية
# ==================================================
class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="المنتج"
    )

    image = CloudinaryField(
        verbose_name="صورة إضافية",
        folder="products/gallery"
    )

    class Meta:
        verbose_name = "صورة منتج"
        verbose_name_plural = "صور المنتجات"

    def __str__(self):
        return f"صورة - {self.product.name}"
