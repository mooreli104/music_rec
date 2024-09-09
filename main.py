import base64, requests, sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Authentication - without user
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

song = input("Song name: ")
artist = input("Artist name: ")
results = sp.search(q= f"track: {song} artist: {artist}")

#List of dictionaries where each dict is a song
list = results["tracks"]["items"]

songs = {}
counter = 0
for x in list:
  songs[counter] = x["name"]
  counter+=1

for key, value in songs.items():
  print(f"{key}: {value}")

choice = int(input("Choose a song number: "))
track_uri = list[choice]["uri"]
list_song_data = ["danceability", "energy", "key", 
                  "loudness", "mode", "speechiness", 
                  "acousticness", "instrumentalness", 
                  "liveness", "valence", "tempo", 
                  "time_signature"]
for x in list_song_data:
  print(sp.audio_features(track_uri)[0][x])



#once user picks a songs, find that songs data and store it. Then use spotyify category_playlist function
#to find a playlist of similar songs. Then interate through the playlist and compare song data with stored data.



