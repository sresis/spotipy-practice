
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def print_all_tracks():
	## birdy album query
	print('---------Birdy albums--------')
	birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
	spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
	results = spotify.artist_albums(birdy_uri, album_type='album')
	albums = results['items']

	while results['next']:
		results = spotify.next(results)
		albums.extend(results['items'])
	for album in albums:
		print(album['name'])

# gets artists info

# def get_artist(name):
#     results = sp.search(q='artist:' + name, type='artist')
#     items = results['artists']['items']
#     if len(items) > 0:
#         return items[0]
#     else:
#         return None

# print(get_artist('Drake'))

# gets Drake albums
def print_all_albums_and_tracks(): 
	print('\n---------Drake albums--------')
	drake_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'
	spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
	results = spotify.artist_albums(drake_uri, album_type='album')
	albums = results['items']

	## prints all albums and album release dates
	while results['next']:
		results = spotify.next(results)
		albums.extend(results['items'])
	#prints all album titles
	for album in albums:
		print(f"Album Title: {album['name']} Release Date: {album['release_date']}")
		print('--------------------------')
		tracks_results = album['uri']
		#gets all tracks in album
		tracks_in_album = spotify.album_tracks(tracks_results)
		for item in tracks_in_album['items']:
			print(item['name'])
		print('------------------------')

print_all_tracks()
print_all_albums_and_tracks()




