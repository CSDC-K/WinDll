import ctypes
from ctypes import wintypes,windll, c_wchar_p, c_void_p, byref, c_long, Structure
import sys
import time



INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002
MAPVK_VK_TO_VSC = 0



if hasattr(wintypes, "ULONG_PTR"):
    ULONG_PTR = wintypes.ULONG_PTR
else:
    if sys.maxsize > 2**32:
        ULONG_PTR = ctypes.c_ulonglong
    else:
        ULONG_PTR = ctypes.c_ulong


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk",      wintypes.WORD),
        ("wScan",    wintypes.WORD),
        ("dwFlags",  wintypes.DWORD),
        ("time",     wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR)
    ]

class INPUT(ctypes.Structure):
    class _I(ctypes.Union):
        _fields_ = [("ki", KEYBDINPUT)]
    _anonymous_ = ("i",)
    _fields_ = [("type", wintypes.DWORD), ("i", _I)]

class User32DLL:
    def __init__(self):
        self.MPOINT = POINT()
        self.user32 = windll.user32
        self.kernel32 = windll.kernel32
        self.WM_CLOSE = 0x0010
        self.user32.FindWindowW.argtypes = [c_wchar_p, c_wchar_p]
        self.user32.FindWindowW.restype = c_void_p

        # USER COMMANDS -->

        self.u_EXECUTESTATION = "SHUTDOWN"
        self.u_LOCKSTATION = "LOCKSTATION"

        self.EWX_LOGOFF = 0
        self.EWX_SHUTDOWN = 0x00000001
        self.EWX_REBOOT = 0x00000002
        self.EWX_FORCE = 0x00000004
        self.EWX_POWEROFF = 0x00000008



        # MOUSE VK CODES -->
        self.LEFT = "LEFT"
        self.RIGHT = "RIGHT"
        self.MIDDLE = "MIDDLE"

        self.SW_HIDE = 0
        self.SW_SHOW = 5

        self.MOUSEEVENTF_LEFTDOWN = 0x0002
        self.MOUSEEVENTF_LEFTUP = 0x0004

        self.MOUSEEVENTF_RIGHTDOWN = 0x0008
        self.MOUSEEVENTF_RIGHTUP = 0x0010

        self.MOUSEEVENTF_MIDDLECLICK = 0x0020 # <-- MOUSE VK CODES

        # KEYBOARD VK CODES -->
        self.VK_LBUTTON = 0x01
        self.VK_RBUTTON = 0x02
        self.VK_CANCEL = 0x03
        self.VK_MBUTTON = 0x04
        self.VK_XBUTTON1 = 0x05
        self.VK_XBUTTON2 = 0x06

        self.VK_BACK = 0x08
        self.VK_TAB = 0x09
        self.VK_CLEAR = 0x0C
        self.VK_RETURN = 0x0D

        self.VK_SHIFT = 0x10
        self.VK_CONTROL = 0x11
        self.VK_MENU = 0x12  # ALT
        self.VK_PAUSE = 0x13
        self.VK_CAPITAL = 0x14  # CAPS LOCK

        self.VK_ESCAPE = 0x1B
        self.VK_SPACE = 0x20
        self.VK_PRIOR = 0x21  # PAGE UP
        self.VK_NEXT = 0x22   # PAGE DOWN
        self.VK_END = 0x23
        self.VK_HOME = 0x24
        self.VK_LEFT = 0x25
        self.VK_UP = 0x26
        self.VK_RIGHT = 0x27
        self.VK_DOWN = 0x28
        self.VK_SELECT = 0x29
        self.VK_PRINT = 0x2A
        self.VK_EXECUTE = 0x2B
        self.VK_SNAPSHOT = 0x2C  # PRINT SCREEN
        self.VK_INSERT = 0x2D
        self.VK_DELETE = 0x2E
        self.VK_HELP = 0x2F


        self.VK_0 = 0x30
        self.VK_1 = 0x31
        self.VK_2 = 0x32
        self.VK_3 = 0x33
        self.VK_4 = 0x34
        self.VK_5 = 0x35
        self.VK_6 = 0x36
        self.VK_7 = 0x37
        self.VK_8 = 0x38
        self.VK_9 = 0x39


        self.VK_A = 0x41
        self.VK_B = 0x42
        self.VK_C = 0x43
        self.VK_D = 0x44
        self.VK_E = 0x45
        self.VK_F = 0x46
        self.VK_G = 0x47
        self.VK_H = 0x48
        self.VK_I = 0x49
        self.VK_J = 0x4A
        self.VK_K = 0x4B
        self.VK_L = 0x4C
        self.VK_M = 0x4D
        self.VK_N = 0x4E
        self.VK_O = 0x4F
        self.VK_P = 0x50
        self.VK_Q = 0x51
        self.VK_R = 0x52
        self.VK_S = 0x53
        self.VK_T = 0x54
        self.VK_U = 0x55
        self.VK_V = 0x56
        self.VK_W = 0x57
        self.VK_X = 0x58
        self.VK_Y = 0x59
        self.VK_Z = 0x5A

        # Numpad
        self.VK_NUMPAD0 = 0x60
        self.VK_NUMPAD1 = 0x61
        self.VK_NUMPAD2 = 0x62
        self.VK_NUMPAD3 = 0x63
        self.VK_NUMPAD4 = 0x64
        self.VK_NUMPAD5 = 0x65
        self.VK_NUMPAD6 = 0x66
        self.VK_NUMPAD7 = 0x67
        self.VK_NUMPAD8 = 0x68
        self.VK_NUMPAD9 = 0x69
        self.VK_MULTIPLY = 0x6A
        self.VK_ADD = 0x6B
        self.VK_SEPARATOR = 0x6C
        self.VK_SUBTRACT = 0x6D
        self.VK_DECIMAL = 0x6E
        self.VK_DIVIDE = 0x6F


        self.VK_F1 = 0x70
        self.VK_F2 = 0x71
        self.VK_F3 = 0x72
        self.VK_F4 = 0x73
        self.VK_F5 = 0x74
        self.VK_F6 = 0x75
        self.VK_F7 = 0x76
        self.VK_F8 = 0x77
        self.VK_F9 = 0x78
        self.VK_F10 = 0x79
        self.VK_F11 = 0x7A
        self.VK_F12 = 0x7B


        self.VK_NUMLOCK = 0x90
        self.VK_SCROLL = 0x91

        self.VK_LSHIFT = 0xA0
        self.VK_RSHIFT = 0xA1
        self.VK_LCONTROL = 0xA2
        self.VK_RCONTROL = 0xA3
        self.VK_LMENU = 0xA4
        self.VK_RMENU = 0xA5 # <--KEYBOARD VK CODES

    def DestroyWindow(self, WindowName: str) -> str:
        hwnd = self.user32.FindWindowW(None, WindowName)
        if hwnd == 0:
            return 0
        self.user32.PostMessageW(hwnd, self.WM_CLOSE, 0, 0)
        self.kernel32.Sleep(500)
        return 1 if self.user32.IsWindow(hwnd) == 0 else 0

    def WindowsKernelAdminIS(self) -> int:
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
    
    def WindowsCall(self, WindowName : str, 
                   SHOW : bool = False, 
                   SetShow : bool = False,
                   SetForeGround : bool = False,
                   SetRes : bool = False,
                   SetPlace : bool = False, 
                   MoveX : int = 100, 
                   MoveY : int = 100, 
                   ResX : int = 500, 
                   ResY : int = 500,
                   SetName : bool = False, 
                   NewName : str = "NONE",
                   SetBlock : bool = False, 
                   SetBlockTime : float = False,
                   BrokeSetBlock : bool = False) -> None:
        hwnd = ctypes.windll.user32.FindWindowW(None, WindowName)
        if SetShow == True:
            if SHOW == True:
                ctypes.windll.user32.ShowWindow(hwnd, self.SW_SHOW)

            elif SHOW == False:
                ctypes.windll.user32.ShowWindow(hwnd, self.SW_HIDE)

        elif SetForeGround == True:
            ctypes.windll.user32.SetForegroundWindow(hwnd)

        elif SetRes == True:
            ctypes.windll.user32.MoveWindow(hwnd, None, None, ResX, ResY, True)

        elif SetPlace == True:
            ctypes.windll.user32.MoveWindow(hwnd, MoveX, MoveY, None, None, True)

        elif SetName == True:
            ctypes.windll.user32.SetWindowTextW(hwnd, NewName)

        elif SetBlock == True:
            if self.WindowsKernelAdminIS:
                if SetBlockTime is not None:
                    ctypes.windll.user32.BlockInput(True)
                    time.sleep(SetBlockTime)
                    ctypes.windll.user32.BlockInput(False)

                elif SetBlockTime is None:
                    ctypes.windll.user32.BlockInput(True)

            else:
                return "Admin Perms Required."

        elif BrokeSetBlock == True:
            ctypes.windll.user32.BlockInput(False)



    def CursorCall(self, SetPos : bool = False,SetPosY : int = 100, SetPosX : int = 100, GetPos : bool = False, ClickEvent = None) -> str:

        if SetPos == True:
            ctypes.windll.user32.SetCursorPos(SetPosX, SetPosY)
        elif GetPos == True:
            ctypes.windll.user32.GetCursorPos(byref(self.MPOINT))
            return "X:" + f"{self.MPOINT.x}" + " Y:" + f"{self.MPOINT.y}"
        elif ClickEvent != None:
            if ClickEvent == self.LEFT:
                ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            
            elif ClickEvent == self.RIGHT:
                ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)   

            elif ClickEvent == self.MIDDLE:
                ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_MIDDLECLICK, 0, 0, 0, 0)


    def KeyboardCall(self, SetPress: bool = False, SetPressTime: float = None, SetPressKey: int = 0) -> None:

        if SetPress:
            if SetPressTime is not None:
                windll.user32.keybd_event(SetPressKey, 0, 0, 0)
                time.sleep(SetPressTime)
                windll.user32.keybd_event(SetPressKey, 0, KEYEVENTF_KEYUP, 0)
            else:
                windll.user32.keybd_event(SetPressKey, 0, 0, 0)
                windll.user32.keybd_event(SetPressKey, 0, KEYEVENTF_KEYUP, 0)


    def UserCall(self, ExecuteW: str = None, DesktopName: str = "Default") -> None:
        if ExecuteW == self.u_LOCKSTATION:
            ctypes.windll.user32.LockWorkStation()

        elif ExecuteW == self.u_EXECUTESTATION:
            ctypes.windll.user32.ExitWindowsEx(self.EWX_SHUTDOWN, 0)

