from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cice_jiit/", views.cice_jiit, name="cice_jiit"),
    path("crescendojiit/", views.crescendojiit, name="crescendojiit"),
    path("gdscjiit/", views.gdscjiit, name="gdscjiit"),
    path("jaypee.photo.enthusiasts.guild/", views.jaypee_photo_enthusiasts_guild, name="jaypee_photo_enthusiasts_guild"),
    path("jhankaarjiit/", views.jhankaarjiit, name="jhankaarjiit"),
    path("jiit.impressions/", views.jiit_impressions, name="jiit_impressions"),
    path("jiityouthclub/", views.jiityouthclub, name="jiityouthclub"),
    path("knuth_jiit/", views.knuth_jiit, name="knuth_jiit"),
    path("nssjiit62/", views.nssjiit62, name="nssjiit62"),
    path("osdcjiit/", views.osdcjiit, name="osdcjiit"),
    path("parola.literaryhub/", views.parola_literaryhub, name="parola_literaryhub"),
    path("radiance.hub/", views.radiance_hub, name="radiance_hub"),
    path("thejaypeedebsoc/", views.thejaypeedebsoc, name="thejaypeedebsoc"),
    path("thepageturnersociety/", views.thepageturnersociety, name="thepageturnersociety"),
    path("thethespiancircle/", views.thethespiancircle, name="thethespiancircle"),
    path("ucrjiit/", views.ucrjiit, name="ucrjiit"),
]