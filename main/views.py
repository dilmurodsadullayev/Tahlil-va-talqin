from django.shortcuts import render, redirect
from .models import CustomUser, Article, View, Team
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.contrib import messages


# Create your views here.


def index_view(request):
    last_article = Article.objects.latest("id")
    print(last_article.image.url)  # 'articles/html_language.jpg' chiqishi kerak
    print(last_article.image.path)

    ctx = {
        "last_article": last_article

    }

    return render(request, "main/index.html", ctx)



def articles_view(request):
    articles = Article.objects.all()

    ctx = {
        "articles": articles
    }
    return render(request, "main/arxiv.html", ctx)


def article_detail(request):
    ctx = {

    }
    return render(request,'main/blog.html', ctx)


def team_view(request):

    teams = Team.objects.all()


    ctx = {
        "teams": teams

    }

    return render(request, 'main/team.html', ctx)

def sequence_view(request):

    ctx = {

    }
    return render(request,'main/sequence.html', ctx)


def news_view(request):

    ctx = {

    }

    return render(request, 'main/news.html', ctx)


def contact_view(request):
    ctx = {

    }

    return render(request, 'main/contact.html', ctx)



def auth_view(request):
    register_form = RegisterForm()
    login_form = LoginForm()

    if request.method == "POST":
        if "signup" in request.POST:  # Agar signup form submit qilinsa
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password(register_form.cleaned_data["password"])  # Parolni hash qilish
                user.save()
                login(request, user)
                # messages.success(request, "Ro'yxatdan o'tish muvaffaqiyatli!")
                return redirect("home")  # Shu sahifaga qaytadi

        elif "login" in request.POST:  # Agar login form submit qilinsa
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                # messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
                return redirect("home")  # Tizimga kirgandan keyin yo'naltirish

    return render(request, 'registration/registration.html', {
        "register_form": register_form,
        "login_form": login_form,
    })

def logout_view(request):
    logout(request)
    messages.success(request, "Tizimdan chiqdingiz!")
    return redirect("home")


def custom_404(request, exception):
    return render(request, '404.html', status=404)