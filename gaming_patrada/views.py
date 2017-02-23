from django.shortcuts import render
from  gaming_patrada.models import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def takehome(response):
    return redirect('/gaming/')


def home(request):
    games = Games.objects.all().order_by('?')[:9]
    slideshow = Games.objects.all().order_by('?')[:3]
    categories = Category.objects.all
    context = {'all_games': games, 'slideshow': slideshow, 'categories': categories}

    return render(request, template_name='gamingpatrada/home.html', context=context)


def category(request, category_name_slug):
    context = {}
    try:
        # bar on top mot important
        categories = Category.objects.all
        context['categories'] = categories
        # bar on top mot important


        category = Category.objects.get(slug=category_name_slug)
        context['category_name'] = category.name
        games_list = Games.objects.filter(category=category).order_by('id')

        paginator = Paginator(games_list, 9)
        page = request.GET.get('page')

        try:
            games = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            games = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            games = paginator.page(paginator.num_pages)

        context['games'] = games
        context['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, template_name='gamingpatrada/category.html', context=context)


def gamedetail(request, category_name_slug, game_name_slug):
    context = {}

    try:
        game = Games.objects.get(slug=game_name_slug)
        game_category = Category.objects.get(slug=category_name_slug)
        related_games = Games.objects.filter(category=game.category).order_by('?')[:4]
        categories = Category.objects.all

        context['relatedgames'] = related_games
        context['game'] = game
        context['categories'] = categories
        context['game_category'] = game_category

    except Games.DoesNotExist:
        pass

    return render(request, template_name='gamingpatrada/gamedetails.html', context=context)


def all_games(request):
    context = {}
    categories = Category.objects.all
    context['categories'] = categories

    # paginator starts here
    ''''''
    allgames = Games.objects.all().order_by('name').exclude(category__id__exact=None)
    paginator = Paginator(allgames, 8)
    page = request.GET.get('page')

    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        games = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        games = paginator.page(paginator.num_pages)

    context['games'] = games
    return render(request, template_name='gamingpatrada/games.html', context=context)


def review(request):
    context = {}
    categories = Category.objects.all
    context['categories'] = categories
    return render(request, template_name='gamingpatrada/review.html', context=context)


def donate(request):
    context = {}
    categories = Category.objects.all
    context['categories'] = categories
    return render(request, template_name='gamingpatrada/Donate.html', context=context)
