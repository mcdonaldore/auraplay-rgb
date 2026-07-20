# AuraPlay RGB - Deployment Guide

## 📦 What's Ready

### Windows Desktop
- ✅ **AuraPlay RGB.exe** - Standalone executable (no Python required)
- ✅ **Build folder** - All necessary dependencies included
- ✅ **installer.iss** - Inno Setup installer script

### Mobile Web Version
- ✅ **web_version/index.html** - Responsive web app
- ✅ Works on iOS Safari and Android Chrome
- ✅ Installable as home screen app

---

## 🚀 Windows Deployment

### Option 1: Direct Use (Recommended for Testing)
```bash
# Just run the exe:
./dist/AuraPlay\ RGB.exe
```

### Option 2: Create Installer
1. **Install Inno Setup**: https://jrsoftware.org/isdl.php
2. **Run the installer script**:
   ```bash
   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
   ```
3. Output will be in `Output/AuraPlay-RGB-Setup.exe`

### Option 3: Distribute as Portable ZIP
```powershell
# Create portable package
Compress-Archive -Path "dist/AuraPlay RGB.exe" -DestinationPath "AuraPlay-RGB-Portable.zip"
```

---

## 📱 Mobile Deployment

### Web Version Setup

#### Deploy to Vercel (Free)
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd web_version
vercel

# Your app will be at: https://yourdomain.vercel.app
```

#### Deploy to GitHub Pages
```bash
# Create repo
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/auraplay-rgb.git
git push -u origin main

# Enable Pages in GitHub Settings
# App will be at: https://yourusername.github.io/auraplay-rgb/
```

#### Deploy to Netlify (Free)
```bash
# Drag and drop web_version folder to:
# https://app.netlify.com/drop
```

### iOS Installation
1. Open web version in Safari
2. Tap Share → Add to Home Screen
3. Creates app-like icon

### Android Installation
1. Open web version in Chrome
2. Tap ⋮ → Install app
3. Creates home screen app

---

## 📥 Download Links Setup

### Create a Releases Page (GitHub)
```bash
# Tag a release
git tag v1.0.0
git push origin v1.0.0

# Upload files:
# - AuraPlay-RGB-Setup.exe (Windows Installer)
# - AuraPlay RGB.exe (Portable)
# - README.md
```

### Self-Hosted Downloads
```bash
# Option 1: Amazon S3
aws s3 cp dist/ s3://mybucket/auraplay-rgb/

# Option 2: Firebase
firebase deploy --only hosting

# Option 3: Simple HTTP Server (Development)
python -m http.server 8000
# Access: http://localhost:8000/dist/
```

---

## 📋 Installation Instructions for Users

### Windows Users
**Option A: Automatic (Recommended)**
- Download `AuraPlay-RGB-Setup.exe`
- Double-click to run installer
- Desktop shortcut created automatically

**Option B: Portable (No Installation)**
- Download `AuraPlay RGB.exe`
- Run directly from any folder
- No installation required

### macOS Users
Coming soon (requires PyInstaller build for macOS)

### Linux Users
Coming soon (requires PyInstaller build for Linux)

### iOS Users
1. Open Safari
2. Visit: `https://your-domain.vercel.app`
3. Tap Share → Add to Home Screen
4. Name: "AuraPlay RGB"
5. Creates app shortcut

### Android Users
1. Open Chrome
2. Visit: `https://your-domain.vercel.app`
3. Tap ⋮ (menu) → Install app
4. Creates home screen app

---

## 🔧 File Structure for Distribution

```
releases/
├── Windows/
│   ├── AuraPlay-RGB-Setup.exe (Installer)
│   ├── AuraPlay RGB.exe (Portable)
│   └── README-Windows.txt
├── Web/
│   ├── index.html
│   └── web_version URL
├── README.md
└── SETUP.md
```

---

## 📊 Recommended Distribution Channels

| Platform | Channel | Free |
|----------|---------|------|
| **Windows** | GitHub Releases | ✅ |
| **Windows** | Microsoft Store | ❌ |
| **iOS** | Web App | ✅ |
| **iOS** | App Store | ❌ |
| **Android** | Web App | ✅ |
| **Android** | Google Play | ❌ |

---

## 🔐 Security Checklist

- [ ] Remove API keys from config.py before distribution
- [ ] Users enter their own Spotify credentials
- [ ] No credentials stored in code
- [ ] Use environment variables for sensitive data
- [ ] HTTPS only for web version
- [ ] Code signed for Windows (optional)

---

## 📈 Download Tracking

### GitHub
```bash
# Automatic tracking via GitHub Releases
# Can see download counts
```

### Analytics
```bash
# Add to web version:
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
</script>
```

---

## 🎯 Next Steps

1. **GitHub**: Create account & repository
2. **Web Hosting**: Choose Vercel/Netlify/GitHub Pages
3. **Inno Setup**: Create installer (Windows)
4. **Upload Files**: Push to releases
5. **Share Links**: Distribute to users

---

## 📞 Support

- Create GitHub Issues for bug reports
- Discord server for community support
- Email: support@auraplay.dev

