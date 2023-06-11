import datetime

import requests
import spotipy
import toml
from spotipy.oauth2 import SpotifyOAuth

from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
format = "%Y-%m-%d"


while(True):
    big_day = input("What day do you want to travel back to? Type the date in YYYY-MM-DD format: ").strip()
    try:
        datetime.datetime.strptime(big_day, format)
        print("This is the correct date string format.")
        break
    except ValueError:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")

resp = requests.get(f"{URL + big_day}/")
resp.raise_for_status()
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup.prettify())
# chart = soup(class_='chart-results')
# pp.pprint(chart)

# titles = soup.find_all('li', class_='o-chart-results-list__item')
titles = soup.select('h3.c-title.a-no-trucate')
titles = [song.text.strip() for song in titles]
# print(len(titles))
# print(titles)
artists = soup.select('span.c-label.a-no-trucate')
artists = [artist.text.strip() for artist in artists]
# print(len(artists))
# print (artists)

config = toml.load(".project_config")
spotify_id = config['spotify']['client_id']
spotify_secret = config['spotify']['secret']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_id, 
                                               client_secret=spotify_secret,
                                               redirect_uri='http://example.com',
                                               scope='playlist-modify-private',
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.me()['id']

uris=[]
for i in range(100):
    # track = f"track: {titles[i]} artist: {artists[i]}"
    track = f"track: {titles[i]} artist:{artists[i]}"
    try:
        tracks = sp.search(track, type='track')  
    except:
        print(f"Couldn't find {track}")
    else:
        print(f"found #{str(i+1)} {track}")
        try:
            uri = tracks['tracks']['items'][0]['uri']
            print(uri)
        except:
            print("no items?")
            print(tracks['tracks'])
            try:
                tracks = sp.search(f"track: {titles[i]}")
                uri = tracks['tracks']['items'][0]['uri']
            except:
                print(f"taking away the artist {artists[i]} didn't work either")
                continue
            else:
                print(f"this worked {uri}")
        uris.append(uri)
        # break
        # pprint.pprint(uri['tracks']['id'])
    
    

# print(uris)
playlist = sp.user_playlist_create(user=user_id, name=f"{big_day} Billboard 100", public=False)
playlist_id = playlist['uri']
print(playlist_id)
sp.playlist_add_items(playlist_id, uris)
# print(sp)




