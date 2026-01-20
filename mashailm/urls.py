from django.contrib import admin
from django.urls import path, include

# إعدادات عرض media و static أثناء التطوير
from django.conf import settings
from django.conf.urls.static import static

# لإيقاف خطأ favicon.ico
from django.views.generic import RedirectView


urlpatterns = [

    # =========================
    # لوحة التحكم
    # =========================
    path('admin/', admin.site.urls),

    # =========================
    # الصفحة الرئيسية
    # =========================
    path('', include('pages.urls')),

    # =========================
    # الحسابات
    # =========================
    path('accounts/', include('accounts.urls')),

    # =========================
    # المتجر
    # =========================
    path('store/', include('store.urls')),

    # =========================
    # الطلبات
    # =========================
    path('orders/', include('orders.urls')),

    # =========================
    # favicon.ico
    # =========================
    path(
        'favicon.ico',
        RedirectView.as_view(
            url=settings.STATIC_URL + 'images/favicon.ico',
            permanent=False
        )
    ),
    path('orders/', include('orders.urls')),

]


# =========================
# دعم ملفات Media أثناء التطوير
# =========================
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
