#Requires AutoHotkey v2.0
#SingleInstance Force

; Run a Python script with AutoHotkey v2
equip_dir := "F:\Repositories\HellDivers2-Loadouts\src\equip" ; Replace with your script's directory
py_script := equip_dir . "/equip.py"

param1 := "loadout1"

; Run the Python script with parameters
Run('python.exe "' . py_script . '" "' . param1 . '"')

keybinds_path := equip_dir . "/cache/" . param1 . ".txt"

if !FileExist(keybinds_path)
{
    MsgBox("Keybinds file not found: " . keybinds_path)
    ExitApp
}

key_dll_map := Map("Space", 0x20, "w", 0x57, "a", 0x41, "s", 0x53, "d", 0x44, "b", 0x42, "r", 0x52, "Escape", 0x1B)

; Read the cached keybinds
keybinds := StrSplit(FileRead(keybinds_path), "`n", "`r")

CapsLock::
{
    ; Send each key
    for key in keybinds {
        if key_dll_map.Has(key) {
            virtual_keybind := key_dll_map[key]
            DllCall("keybd_event", "UInt", virtual_keybind, "UInt", 0, "UInt", 0, "UInt", 0) ; Press
            Sleep(50)
            DllCall("keybd_event", "UInt", virtual_keybind, "UInt", 0, "UInt", 2, "UInt", 0) ; Release
            Sleep(200)
        }
        else {
            MsgBox("Unconfigured key: " . key)
            ExitApp
        }
    }
}