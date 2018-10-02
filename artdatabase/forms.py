from django import forms
from .models import Art, Artist

class ArtForm(forms.ModelForm):

    class Meta:
        model = Art
        fields = ('title', 'artist', 'created',)

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('name',)
      
