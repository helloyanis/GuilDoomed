Add-Type -AssemblyName System.Windows.Forms
Write-Host "Please select the directory you want to get your files in:"
$dialog = New-Object System.Windows.Forms.FolderBrowserDialog
if ($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
    $directoryName = $dialog.SelectedPath
    Write-Host "Directory selected: $directoryName, downloading Python script..."
    Invoke-WebRequest -URI "https://raw.githubusercontent.com/helloyanis/GuilDoomed/main/GuilDOOMed.py" -OutFile $directoryName"\GuilDOOMed.py"
    Write-Host "Downloading Python..."
    winget install Python.Python.3.11
    $pythonVersion = & python --version 2>&1
    if (-not ($pythonVersion -like '*3.10*') -and -not ($pythonVersion -like '*3.11*')) {
        Write-Host "!!WARNING!! Incorrect Python version detected. Please use Python 3.10 or 3.11 instead. You can continue, but there may be errors. I highly recommend you install the correct version instead!"
        Write-Host "Press any key to continue."
        $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    }
    Set-Location $directoryName
    Write-Host "Downloading Python modules..."
    pip install guilded pyautogui aiohttp
    Write-Host ""
    Write-Host "⚠!! READ THIS! ⬇"
    Write-Host "You will need to find a copy of DOOM by yourself, due to legal reasons."
    Write-Host ""
    Write-Host "You need to specify your bot token, create a bot on Guilded, enable API access and copy the token, and paste it in the next prompt, at the variable called 'token'." 
    Write-Host "You will also need to provide the name of the channel you want to input commands in (can only be a text channel), at the variable called 'commands_channel_name'."
    Write-Host "Don't forget to save the file!"
    Write-Host "Press any key to continue and open the file."
    $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    notepad $directoryName"\GuilDOOMed.py"
    Write-Host "You are now done setting up! Read the README on Github on how to start the bot. Press any key to exit."
    $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    
}
else {
    Write-Host "No directory selected"
    $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
