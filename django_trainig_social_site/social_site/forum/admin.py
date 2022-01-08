from django.contrib import admin
from .models import Discussione, Post, Sezione


class DiscusssioneModelAdmin(admin.ModelAdmin):
	model = Discussione
	list_display = ['titolo', 'sezione_apparteneza', 'autore_discuzione']
	search_fields = ['titolo', 'autore_discuzione']
	list_filter = ['sezione_apparteneza', 'data_creazione']


class PostModelAdmin(admin.ModelAdmin):
	model = Post
	list_display = ['autore_post', 'discussione', ]
	search_fields = ['contenuto']
	list_filter = ['data_creazione', 'autore_post']



class SezioneModelAdmin(admin.ModelAdmin):
	model = Sezione
	list_display = ['nome_sezione', 'descrizione']







admin.site.register(Discussione, DiscusssioneModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Sezione, SezioneModelAdmin)






