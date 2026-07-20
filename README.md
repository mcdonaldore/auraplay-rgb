# AuraPlay RGB - Spotify Controller

A stylish RGB Spotify controller application for Windows, macOS, Android, and iOS.

## Features
- Live current song display with album art
- RGB color-changing interface
- Playback controls (Play/Pause, Next, Previous)
- Real-time progress tracking
- Premium & Free account support
- Multi-platform support

## Installation

### Windows

#### Option 1: Standalone Executable (Recommended)
1. Download `AuraPlay-RGB-Setup.exe` from the releases page
2. Run the installer
3. Follow the installation wizard
4. Desktop shortcut will be created automatically
5. Launch from Start Menu or Desktop

#### Option 2: Portable Version
1. Download `AuraPlay-RGB.exe`
2. Place in any folder
3. Double-click to run (no installation required)

### macOS
1. Download `AuraPlay-RGB.dmg`
2. Double-click to mount
3. Drag AuraPlay to Applications folder
4. Launch from Applications

### Linux
```bash
# Extract the archive
tar -xzf AuraPlay-RGB-Linux.tar.gz
cd AuraPlay-RGB
./AuraPlay-RGB
```

### Android / iOS

#### Web Version
1. Visit: [https://auraplay-rgb.vercel.app](https://auraplay-rgb.vercel.app)
2. Save to home screen for app-like experience
3. Scan QR code: (QR code will be provided)

#### Mobile App
- Android: Available on Google Play Store
- iOS: Available on Apple App Store

## First Time Setup

### Get Spotify Credentials
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create an app (free)
3. Copy your **Client ID** and **Client Secret**
4. Set Redirect URI to: `http://127.0.0.1:8888/callback`

### Configure the App
Windows:
- First launch will prompt for credentials
- Enter Client ID and Client Secret
- Authorize with Spotify
- Done!

Web Version:
- Click "Settings" (gear icon)
- Enter your Spotify credentials
- Save

## Requirements

### Spotify Account
- Free or Premium account (Free users can view, Premium users get full control)

### Desktop
- Windows 10/11 (64-bit)
- macOS 10.14+
- Linux (Ubuntu 18.04+)

### Mobile
- iOS 13+
- Android 6.0+

### Internet
- Active internet connection required
- Spotify app running on any device

## Troubleshooting

**"Premium required" error**
- The app owner's Spotify account needs Premium
- Free accounts can view song info but cannot control playback

**Not connecting to Spotify**
1. Ensure Spotify is playing on any device
2. Check internet connection
3. Verify Spotify credentials are correct
4. Restart the app

**"No device found" error**
- Open Spotify on your computer, phone, or web player
- Play a song to activate the device
- Restart AuraPlay

## Source Code
- [GitHub Repository](https://github.com/yourusername/auraplay-rgb)
- MIT License

## Support
- Email: support@auraplay.dev
- Discord: [Join Server](https://discord.gg/)
- Issues: [GitHub Issues](https://github.com/yourusername/auraplay-rgb/issues)
