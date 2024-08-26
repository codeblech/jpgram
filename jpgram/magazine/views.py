from django.shortcuts import render
from django.core.cache import cache
from .models import fetch_index


def index(request):
    return render(request, "base.html")


def cice_jiit(request):
    club = "cice_jiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def crescendojiit(request):
    club = "crescendojiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def gdscjiit(request):
    club = "gdscjiit"
    image_index = fetch_index()
    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jaypee_photo_enthusiasts_guild(request):
    club = "jaypee.photo.enthusiasts.guild"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jhankaarjiit(request):
    club = "jhankaarjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jiit_impressions(request):
    club = "jiit.impressions"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def jiityouthclub(request):
    club = "jiityouthclub"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def knuth_jiit(request):
    club = "knuth_jiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def nssjiit62(request):
    club = "nssjiit62"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def osdcjiit(request):
    club = "osdcjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def parola_literaryhub(request):
    club = "parola.literaryhub"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def radiance_hub(request):
    club = "radiance.hub"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def thejaypeedebsoc(request):
    club = "thejaypeedebsoc"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def thepageturnersociety(request):
    club = "thepageturnersociety"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def thethespiancircle(request):
    club = "thethespiancircle"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )


def ucrjiit(request):
    club = "ucrjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club]}
    )
