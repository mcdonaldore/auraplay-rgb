from server.spotify import get_current_song, is_premium

print("Checking account type...")
if is_premium():
    print("✓ Spotify Premium Account")
else:
    print("Spotify Free Account (some controls may be limited)")

print("\nFetching current song...")
song = get_current_song()

if song:
    print("Now Playing")
    print("--------------------")
    print("Song:", song["song"])
    print("Artist:", song["artist"])
    print("Progress:", f"{song['progress']}ms / {song['duration']}ms")
else:
    print("No song is currently playing.")
