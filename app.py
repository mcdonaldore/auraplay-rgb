from server.spotify import (
    get_current_song,
    get_album_image,
    play_pause,
    next_song,
    previous_song,
    is_premium
)

from PIL import ImageTk

import customtkinter as ctk


# APP SETTINGS

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("500x700")
app.title("Spotify Controller")
app.configure(fg_color="#050505")

# RGB Colors
rgb_colors = [
    "#ff0000",
    "#ff7f00",
    "#ffff00",
    "#00ff00",
    "#00ffff",
    "#0000ff",

    "#8b00ff"
]

color_index = 0


# TITLE

title = ctk.CTkLabel(
    app,
    text="🎮 AuraPlay RGB",
    font=("Arial", 34, "bold")
)
title.pack(pady=20)


# MAIN FRAME

main = ctk.CTkFrame(
    app,
    width=460,
    height=400,
    corner_radius=20,
    fg_color="#111111"
)
main.pack(pady=10)
main.pack_propagate(False)


# ALBUM FRAME

album_frame = ctk.CTkFrame(
    main,
    width=320,
    height=320,
    corner_radius=20,
    border_width=5
)
album_frame.place(x=40, y=50)

album_label = ctk.CTkLabel(
    album_frame,
    text="",
    width=300,
    height=300
)
album_label.place(x=10, y=10)



# SONG INFO

song_label= ctk.CTkLabel(
    main,
    text="No Song Playing",
    font=("Arial", 20, "bold"),

)

song_label.place(x=30, y=250)

artist_label = ctk.CTkLabel(
    main,
    text="",
    font=("Arial", 15)

)
artist_label.place(x=30, y=290)

progress_bar = ctk.CTkProgressBar(main, width=400)
progress_bar.place(x=30, y=330)
progress_bar.set(0)

# BUTTONS

user_is_premium = False

def safe_previous():
    status_label.configure(text_color="#ffaa00")
    status_label.configure(text="Premium required: App owner account needs Premium")
    app.after(3000, lambda: status_label.configure(text_color="#888888"))

def safe_play_pause():
    status_label.configure(text_color="#ffaa00")
    status_label.configure(text="Premium required: App owner account needs Premium")
    app.after(3000, lambda: status_label.configure(text_color="#888888"))

def safe_next():
    status_label.configure(text_color="#ffaa00")
    status_label.configure(text="Premium required: App owner account needs Premium")
    app.after(3000, lambda: status_label.configure(text_color="#888888"))

previous_button = ctk.CTkButton(
    app,
    text="⏮",
    width=80,
    height=50,
    command=safe_previous
)

play_button = ctk.CTkButton(
    app,
    text="▶ / ⏸",
    width=120,
    height=60,
    command=safe_play_pause
)

next_button = ctk.CTkButton(
    app,
    text="⏭",
    width=80,
    height=50,
    command=safe_next
)

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

previous_button.pack(
    in_=button_frame,
    side="left",
    padx=10
)

play_button.pack(
    in_=button_frame,
    side="left",
    padx=10
)

next_button.pack(
    in_=button_frame,
    side="left",
    padx=10
)




# CLOCK

clock = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 18)
)
clock.pack(pady=10)

# STATUS (Premium/Free)

status_label = ctk.CTkLabel(
    app,
    text="Checking account...",
    font=("Arial", 12),
    text_color="#888888"
)
status_label.pack(pady=5)


# ANIMATIONS

def animate():

    global color_index

    color = rgb_colors[color_index]


    title.configure(text_color=color)

    album_frame.configure(border_color=color)

    previous_button.configure(fg_color=color)
    play_button.configure(fg_color=color)
    next_button.configure(fg_color=color)

    color_index = (color_index + 1) % len(rgb_colors)

    app.after(250, animate)

def update_clock():
    try:
        from datetime import datetime
        clock.configure(text=datetime.now().strftime("%H:%M:%S"))
    except Exception as e:
        print(f"Error updating clock: {e}")
    app.after(1000, update_clock)

def update_music():
    try:
        song_data = get_current_song()
        if song_data:
            song_label.configure(text=song_data["song"])
            artist_label.configure(text=song_data["artist"])
            image = get_album_image(song_data["album_art"])
            image = image.resize((300, 300))
            cover = ImageTk.PhotoImage(image)
            album_label.configure(image=cover, text="")
            album_label.image = cover
            if song_data["duration"] > 0:
                progress_bar.set(song_data["progress"] / song_data["duration"])
        else:
            song_label.configure(text="No Song Playing")
            artist_label.configure(text="")
            progress_bar.set(0)
    except Exception as e:
        error_str = str(e)
        if "403" in error_str or "premium" in error_str.lower():
            song_label.configure(text="Premium Account Required")
            artist_label.configure(text="App owner needs Premium")
        else:
            song_label.configure(text="Error loading song")
            artist_label.configure(text="Check your connection")
            print(f"Error updating music: {e}")
    app.after(1000, update_music)


def check_premium_status():
    global user_is_premium
    try:
        user_is_premium = is_premium()
        if user_is_premium:
            status_label.configure(text="✓ Spotify Premium - Full controls enabled", text_color="#00ff41")
        else:
            status_label.configure(text="⚠️ Premium required (app owner needs Premium)", text_color="#ffaa00")
    except Exception as e:
        status_label.configure(text="⚠️ Premium required (app owner needs Premium)", text_color="#ffaa00")
        print(f"Note: App owner account needs Premium for full functionality")
    app.after(30000, check_premium_status)  # Check every 30 seconds

animate()
check_premium_status()
update_clock()
update_music()

app.mainloop()
