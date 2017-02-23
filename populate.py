import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TheGamingPatrada.settings')

import django

django.setup()

from gaming_patrada.models import Games, Category
from django.template.defaultfilters import slugify

def addslugs():
    game_slug = Games.objects.all()
    for game in game_slug:
        game.save()




def remove_duplicate():
    for row in Games.objects.all():
        if Games.objects.filter(cover_photo=row.cover_photo).count() > 1:
            row.delete()

def refreshdb():
    for row in Games.objects.all():
        row.refresh_from_db()

addslugs()