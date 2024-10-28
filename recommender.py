import base64, requests, sys
import spotipy
import librosa
from spotipy.oauth2 import SpotifyClientCredentials

def print_songs(l:list): 
  songs = {}
  counter = 0
  for x in l:
    songs[counter] = x["name"]
    counter+=1

  for key, value in songs.items():
    print(f"{key}: {value}")

# def get_genre(mp3):
#   audio = 


def main():
  #Authentication - without user
  auth_manager = SpotifyClientCredentials()
  sp = spotipy.Spotify(auth_manager=auth_manager)

  song = input("Song name: ")
  artist = input("Artist name: ")
  results = sp.search(q= f"track: {song} artist: {artist}")
  #List of dictionaries where each dict is a song
  list = results["tracks"]["items"]

  print_songs(list)

  choice = int(input("Choose a song number: "))
  
  track_uri = list[choice]["uri"]

  list_song_data = ["danceability", "energy", "key", 
                  "loudness", "mode", "speechiness", 
                  "acousticness", "instrumentalness", 
                  "liveness", "valence", "tempo", 
                  "time_signature"]
  for x in list_song_data:
    print(sp.audio_features(track_uri)[0][x])
    
  #MP3 preview of song
  print(type(list[choice]["preview_url"]))

if __name__ == "__main__":
  main()


#once user picks a songs, find that songs data and store it. Then use spotyify category_playlist function
#to find a playlist of similar songs. Then interate through the playlist and compare song data with stored data.



