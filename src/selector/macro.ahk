#Requires AutoHotkey v2.0

; Run a Python script with AutoHotkey v2
pythonScript := "F:\Repositories\HellDivers2-KitBuilder\src\selector\selector.py" ; Replace with your script's path
Run("python.exe " . pythonScript)
