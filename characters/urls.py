from django.urls import path

from characters.views import get_random_character_view, CharacterListView

urlpatterns = [
    path("character/random/", get_random_character_view, name="random-character"),
    path("character/", CharacterListView.as_view(), name="character-list"),
]

app_name = "characters"
