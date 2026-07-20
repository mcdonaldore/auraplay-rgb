import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
import requests
from PIL import Image
from io import BytesIO

SCOPE = "user-read-currently-playing user-read-playback-state user-read-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
    )
)

def is_premium():
    """Check if user has Spotify Premium"""
    try:
        user_info = sp.current_user()
        return user_info.get("product") == "premium"
    except:
        return False

def get_current_song():
    playback = sp.current_playback()

    if playback and playback["item"]:
        return {
            "song": playback["item"]["name"],
            "artist": playback["item"]["artists"][0]["name"],
            "album_art": playback["item"]["album"]["images"][0]["url"],
            "progress": playback["progress_ms"],
            "duration": playback["item"]["duration_ms"],
        }

    return None


def play_pause():
    try:
        playback = sp.current_playback()
        
        if playback and playback["is_playing"]:
            sp.pause_playback()
        else:
            sp.start_playback()
    except spotipy.exceptions.SpotifyException as e:
        if "PREMIUM_REQUIRED" in str(e):
            print("Premium required: This feature requires Spotify Premium")
        elif "NO_ACTIVE_DEVICE" in str(e):
            print("No active Spotify device found. Open Spotify on a device first.")
        else:
            print(f"Error: {e}")


def next_song():
    try:
        sp.next_track()
    except spotipy.exceptions.SpotifyException as e:
        if "PREMIUM_REQUIRED" in str(e):
            print("Premium required: This feature requires Spotify Premium")
        elif "NO_ACTIVE_DEVICE" in str(e):
            print("No active Spotify device found. Open Spotify on a device first.")
        else:
            print(f"Error: {e}")


def previous_song():
    try:
        sp.previous_track()
    except spotipy.exceptions.SpotifyException as e:
        if "PREMIUM_REQUIRED" in str(e):
            print("Premium required: This feature requires Spotify Premium")
        elif "NO_ACTIVE_DEVICE" in str(e):
            print("No active Spotify device found. Open Spotify on a device first.")
        else:
            print(f"Error: {e}")

def get_progress():
    playback = sp.current_playback()
    if playback and playback["item"]:
        progress = playback["progress_ms"]
        duration = playback["item"]["duration_ms"]

        return progress, duration
    return 0, 0

def get_album_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

