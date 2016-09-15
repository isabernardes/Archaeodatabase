from django.contrib import admin
from .models import Grabung
from .models import Befund
from .models import Profil
from .models import Foto
from .models import Bearbeiter
from .models import GrabBeschreibung

class GrabungModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "nummer"]
	search_fields = ["name", "nummer"]
	class Meta:
		model = Grabung

admin.site.register(Grabung, GrabungModelAdmin)

class BefundModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "deutung", "datum"]
	search_fields = ["name", "nummer"]
	class Meta:
		model = Befund

admin.site.register(Befund, BefundModelAdmin)

class ProfilModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "richtung", "datum"]
	search_fields = ["nummer", "datum"]
	class Meta:
		model = Profil

admin.site.register(Profil, ProfilModelAdmin)

class FotoModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "richtung", "datum"]
	search_fields = ["nummer", "datum"]
	class Meta:
		model = Foto

admin.site.register(Foto, FotoModelAdmin)

class BearbeiterModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "vorname"]
	search_fields = ["name", "vorname"]
	class Meta:
		model = Bearbeiter

admin.site.register(Bearbeiter, BearbeiterModelAdmin)

class GrabBeschreibungModelAdmin(admin.ModelAdmin):
	list_display = ["beschreibung"]
	class Meta:
		model = GrabBeschreibung

admin.site.register(GrabBeschreibung, GrabBeschreibungModelAdmin)