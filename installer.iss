; Inno Setup Script for AuraPlay RGB

[Setup]
AppName=AuraPlay RGB
AppVersion=1.0.0
AppPublisher=AuraPlay
AppPublisherURL=https://github.com
AppSupportURL=https://github.com
AppUpdatesURL=https://github.com
DefaultDirName={pf}\AuraPlay RGB
DefaultGroupName=AuraPlay RGB
LicenseFile=LICENSE.txt
OutputDir=Output
OutputBaseFilename=AuraPlay-RGB-Setup
Compression=lz4
SolidCompression=yes
SetupIconFile=app_icon.ico
UninstallDisplayIcon={app}\AuraPlay RGB.exe
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1,1.1

[Files]
Source: "dist\AuraPlay RGB\AuraPlay RGB.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\AuraPlay RGB\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\AuraPlay RGB"; Filename: "{app}\AuraPlay RGB.exe"; IconFilename: "{app}\app_icon.ico"
Name: "{group}\{cm:UninstallProgram,AuraPlay RGB}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\AuraPlay RGB"; Filename: "{app}\AuraPlay RGB.exe"; IconFilename: "{app}\app_icon.ico"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\AuraPlay RGB"; Filename: "{app}\AuraPlay RGB.exe"; IconFilename: "{app}\app_icon.ico"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\AuraPlay RGB.exe"; Description: "{cm:LaunchProgram,AuraPlay RGB}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
