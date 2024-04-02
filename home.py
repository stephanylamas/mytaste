#install spotipy with pip/pip3 install spotipy

#import spotipy
import spotipy, pandas as pd
from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='018b4e619c804822aedcfcc66e3257aa', client_secret='3aae70543b6247d9aa1a3932f66d4644', redirect_uri='http://localhost:8888/callback', scope='user-top-read'))
#print(sp)

# Example: Get audio features of a track
track_id = '6rqhFgbbKwnb9MLmUQDhG6'
audio_features = sp.audio_features(tracks=[track_id])
#print out audio features of the example track 
print(audio_features)

# Retrieve the top 50 tracks for the current user (short-term time range)
top_tracks_1 = sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')

# Retrieve the next 50 tracks for the current user (short-term time range)
top_tracks_2 = sp.current_user_top_tracks(limit=50, offset=50, time_range='short_term')

# Combine the results from both requests to get the top 100 tracks
top_100_tracks = top_tracks_1['items'] + top_tracks_2['items']

for idx, track in enumerate(top_100_tracks):
    try:
        print(f"{idx + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
    except UnicodeEncodeError:
        print(f"{idx + 1}. [Track name or artist name contains non-encodable characters]")

#retrieve track id for each of your top 100 songs
trackDetails = []
for track in top_100_tracks:
    track_id = track['id']
    #debugging print statement
    #print(track_id)
    track_info = sp.track(track_id)
    trackDetails.append(track_info)

#personally this prints our the track Details for Work Bitch by Britney Spears
print(trackDetails[0])

