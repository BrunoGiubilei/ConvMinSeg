[Setup]
AppName=ConvMinSeg
AppVersion=1.0
DefaultDirName={pf}\ConvMinSeg
OutputDir=.
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\workspace\ConvMinSeg\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ConvMinSeg"; Filename: "{app}\main.exe"
Name: "{commondesktop}\ConvMinSeg"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar um ícone na área de trabalho"; GroupDescription: "Atalhos adicionais:"
