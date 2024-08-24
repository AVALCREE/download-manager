[Setup]
AppName=Download Manager
AppVersion=1.0
DefaultDirName={pf}\Download Manager
DefaultGroupName=Download Manager
OutputDir=userdocs\Inno Setup Examples
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
; Batch file to install Python and run the Python script
Source: "install_and_run.bat"; DestDir: "{app}"; Flags: ignoreversion
; Python script
Source: "main.py"; DestDir: "{app}"; Flags: ignoreversion
; Optional: Python installer if you want to bundle it
; Source: "python_installer.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall

[Icons]
; Create a shortcut in the Start Menu group
Name: "{group}\Download Manager"; Filename: "{app}\install_and_run.bat"
; Create a shortcut on the Desktop
Name: "{desktop}\Download Manager"; Filename: "{app}\install_and_run.bat"

[Run]
; Run the batch file to ensure Python is installed and to start the script
Filename: "{app}\install_and_run.bat"; WorkingDir: "{app}"; Flags: nowait postinstall skipifsilent
