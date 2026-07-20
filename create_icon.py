"""
Create Spotify app icon using PIL
Spotify color: #1DB954 (green)
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create icon image (256x256)
img = Image.new('RGB', (256, 256), color='#1DB954')
draw = ImageDraw.Draw(img)

# Draw spotify circle
draw.ellipse([20, 20, 236, 236], fill='#1DB954', outline='#1DB954')

# Try to add text, fallback if font not available
try:
    font = ImageFont.truetype("arial.ttf", 100)
except:
    font = ImageFont.load_default()

# Draw music note or S symbol
draw.text((85, 70), "S", fill='white', font=font)

# Save as PNG and ICO
img.save('app_icon.png')
print("Created app_icon.png")

# Convert to ICO
img.save('app_icon.ico', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
print("Created app_icon.ico")
