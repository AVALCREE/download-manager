!include "MUI2.nsh"

; Name of the installer
Name "My Python Application"
; Output file name
OutFile "SetupMyPythonApp.exe"
; Directory where the application will be installed
InstallDir "$PROGRAMFILES\MyPythonApp"
; Request admin rights
RequestExecutionLevel admin

; Pages to show during installation
Page directory
Page instfiles

; Section for installing the application
Section "MainSection"
    ; Set the output directory to the installation folder
    SetOutPath "$INSTDIR"
    ; Include files in the installer
    File "main.py"
    File "install_and_run.bat"
    File "python-setup.exe"

    ; Run the batch file to install Python and start the application
    ExecShell "runas" "$INSTDIR\install_and_run.bat"
SectionEnd
