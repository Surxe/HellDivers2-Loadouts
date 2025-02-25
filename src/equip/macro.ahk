#Requires AutoHotkey v2.0
#SingleInstance Force

; Run a Python script with AutoHotkey v2
equip_dir := "F:\Repositories\HellDivers2-Loadouts\src\equip" ; Replace with your script's directory
py_script := equip_dir . "/equip.py"
Run("python.exe " . py_script)

param1 := "loadout1"

; Run the Python script with parameters
Run('python.exe "' . py_script . '" "' . param1 . '"')

keybinds_path := equip_dir . "/cache/" . param1 . ".txt"

if !FileExist(keybinds_path)
{
    MsgBox("Keybinds file not found: " . keybinds_path)
    ExitApp
}

; Read the cached keybinds
keybinds := StrSplit(FileRead(keybinds_path), " ")

CapsLock::
{
    ; Send each key
    for key in keybinds {
        if key != "" {
            Send(key)
            Sleep(100)
        }
    }
}