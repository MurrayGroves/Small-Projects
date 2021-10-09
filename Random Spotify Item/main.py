import tekore as tk
import random

CLIENT_ID = "051c9a00ca874689a506bf581ae451a1"

try:
    f = open("token.dat")
    token = f.read()
    f.close()
    token = tk.refresh_pkce_token(CLIENT_ID, token)

except:
    token = tk.prompt_for_pkce_token(client_id=CLIENT_ID, scope=None, redirect_uri="https://google.com")

f = open("token.dat", "w+")
f.write(token.refresh_token)
f.close()

spotify = tk.Spotify(token)

while True:
    category = input("What type of item do you want to find? (artist, album, track, playlist, show, episode)\n")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char = alphabet[random.randint(0, 25)]
    offset = random.randint(0, 950)
    search = spotify.search(f"{char}%", types=(category,), limit=50, include_external="audio", offset=offset)
    print(f"https://open.spotify.com/{category}/" + random.choice(search[0].items).id)
