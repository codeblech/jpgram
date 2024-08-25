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

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def crescendojiit(request):
    club = "crescendojiit"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def gdscjiit(request):
    club = "gdscjiit"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jaypee_photo_enthusiasts_guild(request):
    club = "jaypee.photo.enthusiasts.guild"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jhankaarjiit(request):
    club = "jhankaarjiit"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jiit_impressions(request):
    club = "jiit.impressions"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jiityouthclub(request):
    club = "jiityouthclub"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def knuth_jiit(request):
    club = "knuth_jiit"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def nssjiit62(request):
    club = "nssjiit62"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def osdcjiit(request):
    club = "osdcjiit"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def parola_literaryhub(request):
    club = "parola.literaryhub"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def radiance_hub(request):
    club = "radiance.hub"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def thejaypeedebsoc(request):
    club = "thejaypeedebsoc"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def thepageturnersociety(request):
    club = "thepageturnersociety"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def thethespiancircle(request):
    club = "thethespiancircle"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def ucrjiit(request):
    club = "ucrjiit"

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )
