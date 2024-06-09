from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Article, ArticleImage, HistoricalPerson, ArticleScope
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

User = get_user_model()


def index(request):
    title = request.GET.get('query')
    if title:
        articles = Article.objects.filter(
            Q(title__icontains=title) | Q(persons__full_name=title) | Q(scope__scope=title)
        )
    else:
        articles = Article.objects.all()
    actors = HistoricalPerson.objects.all()
    spheres = ArticleScope.objects.all()
    context = {
        'articles': articles,
        'title': title,
        'actors': actors,
        'spheres': spheres,
    }
    return render(request, 'app_advertisements/index.html', context)


@login_required(login_url=reverse_lazy('login'))
def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }
    return render(request, 'app_advertisements/advertisement.html', context)


@login_required(login_url=reverse_lazy('login'))
def article_post(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False, author=request.user)
            url = reverse('main-page')
            return redirect(url)
    else:
        form = ArticleForm()
    is_moderator = request.user.groups.filter(name="Модератор").exists()
    context = {'form': form, "is_moderator": is_moderator}
    return render(request, 'app_advertisements/advertisement-post.html', context)


def add_files(files, instance):
    for file in files:
        ArticleImage.objects.create(
            image=file,
            article=instance,
        )
