import os
import django
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TheGamingPatrada.settings')

django.setup()

from gaming_patrada.models import *
from django.template.defaultfilters import slugify
from igdb.requester import Requester
from igdb import Filter
from igdb.operators import GTE, GT, EQ, EXISTS, PREFIX
import urllib,lxml
from gamesdb.api import API
from lxml import etree


def add_slugs():
    game_slug = Games.objects.all()
    for game in game_slug:
        game.slug = slugify(game.name)
        game.save()
        print('adding slug to ' + game.name)


def remove_duplicate():
    for row in Games.objects.all():
        if Games.objects.filter(cover_photo=row.cover_photo).count() > 1:
            row.delete()


def refresh_db():
    for row in Games.objects.all():
        row.refresh_from_db()


def add_letters():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V",
               "W", "X", "Y", "Z"]
    for letter in letters:
        let = Letters(letters=letter)
        let.save()

        print('adding letter ' + '' + letter + ' ' + 'to letters')


def igdb_get():
    api_key = 'HpEHD4xuXPmshMfE99fmqesgjbJmp16vdTYjsn7tWoAYgKNbdI'
    req = Requester(api_key)
    game=Games.objects.get(id=200)
    print('looking for '+game.name)
    filter_slug = Filter(field='slug', operator=EQ, value=game.slug)
    #filter_name = Filter(field='name', operator=EQ, value=game.name)

    print(req.get_games(fields='name,slug,release_dates.human', limit=1, offset=0, order='release_dates.date:desc',
                        filters=[filter_slug]))



def thegamesdb():
    gamesdb_api = API()
    platform_list = gamesdb_api.get_platforms_list()
    for platform in platform_list:
        print(
        platform.id, "-", platform.name, "-", platform.alias)

games = Games.objects.all()
def releasedates():
    for game in games:
        print('looking for '+game.name)
        try:
            request = etree.parse('http://thegamesdb.net/api/GetGame.php?name='+game.name)
            gametag = request.find('Game')
            datetag = gametag.find('ReleaseDate')
            datetext = datetag.text
            newdate = datetime.datetime.strptime(datetext, '%m/%d/%Y').strftime('%Y-%m-%d')
            ratingTag = gametag.find('Rating')
            rating = ratingTag.text
            print(newdate)

            game.release=newdate
            game.rating = rating
            game.save()
        except:
            print('game not found')
def rating():

    for game in games:
        try:
            print('looking for ' + game.name)
            request = etree.parse('http://thegamesdb.net/api/GetGame.php?name=' + game.name)
            gametag = request.find('Game')
            ratingTag = gametag.find('Rating')
            rating = ratingTag.text
            rating=float(rating)
            game.rating=rating
            print(rating)


        except :
            pass

def adddates():
    for game in games:
        try:
            print('looking for ' + game.name)
            request = etree.parse('http://thegamesdb.net/api/GetGame.php?name=' + game.name)
            gametag = request.find('Game')
            datetag = gametag.find('ReleaseDate')
            datetext = datetag.text
            newdate = datetime.datetime.strptime(datetext, '%m/%d/%Y').strftime('%Y-%m-%d')
            print(newdate)

            game.release = newdate
            game.save()

        except:
            pass