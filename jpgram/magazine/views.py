from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os


def index(request):
    return render(request, "base.html")


def cice_jiit(request):
    return HttpResponse("Hello, world. You're at the CICE JIIT homepage.")


def crescendojiit(request):
    return HttpResponse("Hello, world. You're at the Crescendo JIIT homepage.")


def gdscjiit(request):
    return HttpResponse("Hello, world. You're at the GDSC JIIT homepage.")


def jaypee_photo_enthusiasts_guild(request):
    return HttpResponse(
        "Hello, world. You're at the Jaypee Photo Enthusiasts Guild homepage."
    )


def jhankaarjiit(request):
    return HttpResponse("Hello, world. You're at the Jhankaar JIIT homepage.")


def jiit_impressions(request):
    return HttpResponse("Hello, world. You're at the JIIT Impressions homepage.")


def jiityouthclub(request):
    return HttpResponse("Hello, world. You're at the JIIT Youth Club homepage.")


def knuth_jiit(request):
    return HttpResponse("Hello, world. You're at the Knuth JIIT homepage.")


def nssjiit62(request):
    return HttpResponse("Hello, world. You're at the NSS JIIT 62 homepage.")


def osdcjiit(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "osdcjiit"
    )

    # Collect all the image filenames
    image_list = []
    if os.path.exists(static_dir):
        for filename in os.listdir(static_dir):
            if filename.endswith((".jpg", ".jpeg", ".png")):
                image_list.append(f"magazine/osdcjiit/{filename}")

    return render(request, "magazine/osdcjiit.html", {"images": image_list})


def parola_literaryhub(request):
    return HttpResponse("Hello, world. You're at the Parola Literary Hub homepage.")


def radiance_hub(request):
    return HttpResponse("Hello, world. You're at the Radiance Hub homepage.")


def thejaypeedebsoc(request):
    return HttpResponse("Hello, world. You're at The Jaypee Debating Society homepage.")


def thepageturnersociety(request):
    return HttpResponse("Hello, world. You're at The Page Turner Society homepage.")


def thethespiancircle(request):
    return HttpResponse("Hello, world. You're at The Thespian Circle homepage.")


def ucrjiit(request):
    return HttpResponse("Hello, world. You're at the UCR JIIT homepage.")
