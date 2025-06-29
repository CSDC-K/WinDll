# 🚀 WinDll 0.1.0

![Python](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Version](https://img.shields.io/badge/version-0.1.0-orange) 
## 🔥 What is WinDll?

WinDll is a lightweight Python wrapper around Windows' native `user32.dll` and `kernel32.dll` APIs designed to simplify common Windows system tasks such as window management, keyboard/mouse input simulation, process management, and system control.

This library allows Python developers to automate and control Windows OS functions easily **without external dependencies**, using only `ctypes`.

---

## 🛠 Features

- 🖥️ Window management (find, move, resize, show/hide, set foreground)
- ⌨️ Keyboard input simulation (`SendInput` wrapper)
- 🖱️ Mouse input simulation (move cursor, click)
- 🔒 Block and unblock user input (`BlockInput`)
- 🧑‍💼 Check if script runs with admin privileges
- ❌ Kill processes by executable name (pure ctypes implementation)
- 🚪 Lock workstation or reboot system

---

## 📚 Installation

```bash
pip install windll-python
```

---

## 💡 Usage Examples

### Initialization

```python
from WinDll import User32DLL, Kernel32DLL

winapi = User32DLL()
#or
winapi = Kernel32DLL
```

---

### Window Operations - USER32

```python
# Close a window by title
result = winapi.DestroyWindow("Untitled - Notepad")
print("Closed successfully" if result else "Window not found")

# Show or hide a window
winapi.WindowsCall(WindowName="Untitled - Notepad", SetShow=True, SHOW=True)  # Show window
winapi.WindowsCall(WindowName="Untitled - Notepad", SetShow=True, SHOW=False) # Hide window

# Set window to foreground
winapi.WindowsCall(WindowName="Untitled - Notepad", SetForeGround=True)

# Move and resize window
winapi.WindowsCall(WindowName="Untitled - Notepad", SetRes=True, ResX=800, ResY=600)
winapi.WindowsCall(WindowName="Untitled - Notepad", SetPlace=True, MoveX=100, MoveY=100)
# Rename Window
winapi.WindowsCall(WindowName="Untitled - Notepad", SetName = True, NewName = "Test - Notepad")
```

---

### Keyboard Simulation - USER32

```python
# Press and release 'A' key quickly
winapi.KeyboardCall(SetPress=True, SetPressKey=winapi.VK_A)

# Press 'A' key for 2 seconds
winapi.KeyboardCall(SetPress=True, SetPressTime=2.0, SetPressKey=winapi.VK_A)


```

---

### Mouse Simulation - USER32

```python
# Move cursor to (500, 500)
winapi.CursorCall(SetPos=True, SetPosX=500, SetPosY=500)

# Get current cursor position
pos = winapi.CursorCall(GetPos=True)
print(pos)  # Output: X:xxx Y:yyy

# Left click
winapi.CursorCall(ClickEvent=winapi.LEFT)

# Right click
winapi.CursorCall(ClickEvent=winapi.RIGHT)
```

---

### Blocking User Input - USER32

```python
# Block mouse and keyboard input for 5 seconds
winapi.WindowCall(SetBlock=True, SetBlockTime=5)

# Unblock input manually
winapi.WindowCall(BrokeSetBlock=True)
```

---

### Process Management - KERNEL32

```python
# Kill all notepad.exe processes
winapi.KernelCall(process=wina.kernel_PROCESSEXECUTE, ProcessPath="notepad.exe")

# Start Process
winapi.KernelCall(process=wina.kernel_PROCESSCREATE, ProcessPath="path")


```

---

### Check Admin Rights - USER32

```python
if winapi.WindowsKernelAdminIS():
    print("Running as administrator")
else:
    print("Not running as administrator")
```

---

## 📝 License

This project is licensed under the MIT License.

---

## 🙋 Author

**CSDC-K VV**

---

## ⭐ Contributions Welcome!

Feel free to open issues or submit pull requests.

---

## 📌 Disclaimer

Use with caution. Some functions (e.g., `TerminateProcess`, `BlockInput`) affect system stability or user control.

---

Enjoy coding with WinDll! 🚀
