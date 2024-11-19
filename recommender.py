import base64, requests, sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def print_songs(l:list): 
  songs = {}
  counter = 0
  for x in l:
    songs[counter] = x["name"]
    counter+=1

  for key, value in songs.items():
    print(f"{key}: {value}")

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
  track_id =[list[choice]["id"]]

  
  list_song_data = ["danceability", "energy", "key", 
                  "loudness", "mode", "speechiness", 
                  "acousticness", "instrumentalness", 
                  "liveness", "valence", "tempo", 
                  "time_signature"]

  song_data = []
  for x in list_song_data:
    song_data.append(sp.audio_features(track_uri)[0][x])
  
  #Get the artist spotify ID and use to search list of his/her genre(s)
  artist_id= [list[choice]["artists"][0]["id"]]
  artist_genres = sp.artist(artist_id[0])["genres"]

  recommendations = sp.recommendations(artist_id, artist_genres,track_id, 20, "",
                           danceability = song_data[0], energy = song_data[1],
                           key = song_data[2], loudness = song_data[3],
                           mode = song_data[4], speechiness = song_data[5],
                           acousticness = song_data[6], instrulmentalness = song_data[7],
                           liveness = song_data[8], valence = song_data[9],
                           temp = song_data[10], time_signature = song_data[11], popularity = 50)
  
  print("\n")


  for x in recommendations["tracks"]:
    print(x["name"] + " " + x["artists"][0]["name"])


  #MP3 preview of song
  #print(type(list[choice]["preview_url"]))

if __name__ == "__main__":
  main()



