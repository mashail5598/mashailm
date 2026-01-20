from django.db import models
from accounts.models import User
from store.models import Product


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name="المستخدم"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    class Meta:
        verbose_name = "سلة"
        verbose_name_plural = "السلال"

    def __str__(self):
        return f"سلة {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="السلة"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="المنتج"
    )

    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="الكمية"
    )

    class Meta:
        verbose_name = "عنصر سلة"
        verbose_name_plural = "عناصر السلة"

    def __str__(self):
        return f"{self.product} × {self.quantity}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'جديد'),
        ('paid', 'مدفوع'),
        ('shipped', 'تم الشحن'),
        ('done', 'مكتمل'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name="المستخدم"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name="حالة الطلب"
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="إجمالي السعر"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الطلب"
    )

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="الطلب"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="المنتج"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )

    quantity = models.PositiveIntegerField(
        verbose_name="الكمية"
    )

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.product} × {self.quantity}"
