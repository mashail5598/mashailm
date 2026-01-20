from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Cart, CartItem
from store.models import Product


@login_required
def add_to_cart(request, product_id):
    """
    إضافة منتج إلى السلة ثم الانتقال لصفحة السلة
    """

    product = get_object_or_404(Product, id=product_id)

    # إنشاء سلة للمستخدم إذا لم تكن موجودة
    cart, created = Cart.objects.get_or_create(user=request.user)

    # إضافة المنتج أو زيادة الكمية
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    # بعد الإضافة → عرض السلة
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    """
    عرض محتويات السلة
    """

    cart, created = Cart.objects.get_or_create(user=request.user)

    return render(
        request,
        "orders-templates/cart.html",
        {
            "cart": cart,
            "items": cart.items.all()
        }
    )
