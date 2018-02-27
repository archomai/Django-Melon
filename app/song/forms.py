from django import forms

from .models import Song

__all__ = (
    'SongForm',
)


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            'title',
            'genre',
            'lyrics',
        ]
