'''
To get client ID and client secret, go to https://developer.spotify.com/dashboard
Then, log in with your Spotify Account and create an app
You can see the Client ID of the app right from the dasboard. Copy the CLient ID and replace it with client_id_here
To see the Client Secret, click on the app and then on "SHOW CLIENT SECRET". Copy the Secret and replace it with client_secret_here
Replace user_id_here with your spotify username
'''

SPOTIPY_CLIENT_ID='client_id_here'
SPOTIPY_CLIENT_SECRET='client_secret_here'
SPOTIPY_REDIRECT_URI='http://example.com'
USER = 'user_id_here'

import json
import spotipy

scope = 'user-read-currently-playing user-library-modify user-library-read playlist-modify-public'

token = spotipy.util.prompt_for_user_token(USER, scope = scope, client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET, redirect_uri = SPOTIPY_REDIRECT_URI)

music = spotipy.Spotify(auth = token)
currentPlay = music.currently_playing()
userPlaylist = music.current_user_playlists()
userSavedTrack = music.current_user_saved_tracks(limit = 20)

newP_id = userPlaylist['items'][0]['id']
newP_name = userPlaylist['items'][0]['name']

newP = music.playlist_tracks(newP_id, limit = 20)

for i in range(len(userSavedTrack['items'])):
    trackID_liked = userSavedTrack['items'][i]['track']['id']
    
    for j in range(len(newP['items'])):
        trackID_newP = newP['items'][j]['track']['id']
        flag = 0
        
        if (trackID_newP == trackID_liked):
            flag = 1
            break
    
    if (flag == 0):
        print(f"Found new track.")
        trackName = userSavedTrack['items'][i]['track']['name']
        print(f"Name: {trackName}")
        print(f"Adding new track to Playlist: {newP_name}")
        music.user_playlist_add_tracks(USER, newP_id, [trackID_liked], position = 0)
        print("Track successfully added!")

