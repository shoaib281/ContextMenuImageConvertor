import os
os.system("pip install Pillow")

import winreg

cmdLocation = os.path.dirname(__file__) + "\imageConvertor.cmd %1"
cmdLocation.encode("unicode_escape")

keyName =  r"ConvertImage"
setValue = r"Image2Jpeg"

keyLocation = r"*\shell\ConvertImage"

reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)

key = winreg.CreateKey(reg, keyLocation)
winreg.SetValue(reg, keyLocation,winreg.REG_SZ,setValue)

newKey = winreg.CreateKey(key, "command")
winreg.SetValue(key, "command",winreg.REG_SZ,cmdLocation)

