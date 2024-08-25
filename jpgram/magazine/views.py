from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
import os
from .models import image_index


def index(request):
    return render(request, "base.html")


def cice_jiit(request):
    club = "cice_jiit"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def crescendojiit(request):
    club = "crescendojiit"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def gdscjiit(request):
    club = "gdscjiit"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jaypee_photo_enthusiasts_guild(request):
    club = "jaypee.photo.enthusiasts.guild"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jhankaarjiit(request):
    club = "jhankaarjiit"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jiit_impressions(request):
    club = "jiit.impressions"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jiityouthclub(request):
    club = "jiityouthclub"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def knuth_jiit(request):
    club = "knuth_jiit"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def nssjiit62(request):
    club = "nssjiit62"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def osdcjiit(request):
    club = "osdcjiit"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def parola_literaryhub(request):
    club = "parola.literaryhub"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def radiance_hub(request):
    club = "radiance.hub"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def thejaypeedebsoc(request):
    club = "thejaypeedebsoc"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def thepageturnersociety(request):
    club = "thepageturnersociety"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def thethespiancircle(request):
    club = "thethespiancircle"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def ucrjiit(request):
    club = "ucrjiit"
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", club
    )
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )
