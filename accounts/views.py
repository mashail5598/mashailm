from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("home")



# ============================
# إنشاء حساب جديد
# ============================
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # التحقق من المدخلات
        if password1 != password2:
            messages.error(request, "كلمتا المرور غير متطابقتين")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم مسبقًا")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مستخدم مسبقًا")
            return redirect("register")

        # إنشاء المستخدم
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        login(request, user)
        return redirect("home")  # عدلها حسب صفحتك الرئيسية

    return render(request, "accounts-templates/register.html")


# ============================
# تسجيل الدخول
# ============================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "بيانات الدخول غير صحيحة")

    return render(request, "accounts-templates/login.html")
