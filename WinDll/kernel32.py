import ctypes 
from ctypes import *
from ctypes import wintypes


kernel32 = windll.kernel32
psapi = ctypes.WinDLL('psapi', use_last_error=True)
STARTUPINFO = ctypes.Structure
PROCESS_INFORMATION = ctypes.Structure


PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010
PROCESS_TERMINATE = 0x0001
MAX_PATH = 260

class STARTUPINFO(ctypes.Structure):
    _fields_ = [
        ('cb',              wintypes.DWORD),
        ('lpReserved',      wintypes.LPWSTR),
        ('lpDesktop',       wintypes.LPWSTR),
        ('lpTitle',         wintypes.LPWSTR),
        ('dwX',             wintypes.DWORD),
        ('dwY',             wintypes.DWORD),
        ('dwXSize',         wintypes.DWORD),
        ('dwYSize',         wintypes.DWORD),
        ('dwXCountChars',   wintypes.DWORD),
        ('dwYCountChars',   wintypes.DWORD),
        ('dwFillAttribute', wintypes.DWORD),
        ('dwFlags',         wintypes.DWORD),
        ('wShowWindow',     wintypes.WORD),
        ('cbReserved2',     wintypes.WORD),
        ('lpReserved2',     ctypes.POINTER(ctypes.c_byte)),
        ('hStdInput',       wintypes.HANDLE),
        ('hStdOutput',      wintypes.HANDLE),
        ('hStdError',       wintypes.HANDLE),
    ]

class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('hProcess',    wintypes.HANDLE),
        ('hThread',     wintypes.HANDLE),
        ('dwProcessId', wintypes.DWORD),
        ('dwThreadId',  wintypes.DWORD),
    ]

class SYSTEM_INFO(ctypes.Structure):
    class _U(ctypes.Union):
        class _W(ctypes.Structure):
            _fields_ = [
                ("wProcessorArchitecture", ctypes.c_ushort),
                ("wReserved", ctypes.c_ushort)
            ]
        _fields_ = [
            ("dwOemId", ctypes.c_ulong),
            ("w", _W)
        ]
    _anonymous_ = ("u",)
    _fields_ = [
        ("u", _U),
        ("dwPageSize", ctypes.c_ulong),
        ("lpMinimumApplicationAddress", ctypes.c_void_p),
        ("lpMaximumApplicationAddress", ctypes.c_void_p),
        ("dwActiveProcessorMask", ctypes.c_void_p),
        ("dwNumberOfProcessors", ctypes.c_ulong),
        ("dwProcessorType", ctypes.c_ulong),
        ("dwAllocationGranularity", ctypes.c_ulong),
        ("wProcessorLevel", ctypes.c_ushort),
        ("wProcessorRevision", ctypes.c_ushort)
    ]


class MEMORYSTATUSEX(ctypes.Structure):
    _fields_ = [
        ("dwLength", ctypes.c_ulong),
        ("dwMemoryLoad", ctypes.c_ulong),
        ("ullTotalPhys", ctypes.c_ulonglong),
        ("ullAvailPhys", ctypes.c_ulonglong),
        ("ullTotalPageFile", ctypes.c_ulonglong),
        ("ullAvailPageFile", ctypes.c_ulonglong),
        ("ullTotalVirtual", ctypes.c_ulonglong),
        ("ullAvailVirtual", ctypes.c_ulonglong),
        ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
    ]

def get_all_pids():
    arr = (wintypes.DWORD * 1024)()
    cb = ctypes.sizeof(arr)
    bytes_returned = wintypes.DWORD()

    if not psapi.EnumProcesses(arr, cb, ctypes.byref(bytes_returned)):
        raise ctypes.WinError(ctypes.get_last_error())

    count = int(bytes_returned.value / ctypes.sizeof(wintypes.DWORD))
    return arr[:count]

# Process adı al
def get_process_name(pid):
    h_process = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
    if not h_process:
        return None

    exe_name = (ctypes.c_wchar * MAX_PATH)()
    if psapi.GetModuleBaseNameW(h_process, None, exe_name, MAX_PATH) > 0:
        kernel32.CloseHandle(h_process)
        return exe_name.value
    kernel32.CloseHandle(h_process)
    return None





class Kernel32DLL:


    def __init__(self):
        self.windll = ctypes.windll
        self.user32 = ctypes.windll.user32
        self.kernel32 = ctypes.windll.kernel32
        
        self.kernel_BEEP = "BEEP"
        self.kernel_PROCESSINFO = "PROCESSINFO"
        self.kernel_RAMEX = "RAMEX"
        self.kernel_PROCESSCREATE = "PROCESSCREATE"
        self.kernel_PROCESSEXECUTE = "PROCESSEXECUTE"




    def KernelCall(self, process : str = None, AppPath : str = "main.exe", BPms : int = 1000, BPhz : int = 750,ProcessPath : str = None) -> None:
        
        if process == self.kernel_PROCESSINFO:
            sysInfo = SYSTEM_INFO()
            self.kernel32.GetSystemInfo(ctypes.byref(sysInfo))

            return sysInfo.dwNumberOfProcessors  

        elif process == self.kernel_RAMEX:
            mem_stat = MEMORYSTATUSEX()
            mem_stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)

            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem_stat))          

            return mem_stat.ullTotalPhys // 1024**2
        
        elif process == self.kernel_BEEP:
            self.kernel32.Beep(BPhz,BPms)

        elif process == self.kernel_PROCESSCREATE:
            si = STARTUPINFO()
            si.cb = ctypes.sizeof(si)
            pi = PROCESS_INFORMATION()

            success = windll.kernel32.CreateProcessW(
                None,
                ProcessPath,
                None,
                None,
                False,
                0,
                None,
                None,
                ctypes.byref(si),
                ctypes.byref(pi)
            )

            if not success:
                raise ctypes.WinError(ctypes.get_last_error())
            
            else:
                return pi.dwProcessId
            
        
        elif process == self.kernel_PROCESSEXECUTE:
            pids = get_all_pids()
            for pid in pids:
                name = get_process_name(pid)
                if name and name.lower() == ProcessPath.lower():
                    h_process = kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)
                    if h_process:
                        kernel32.TerminateProcess(h_process, 0)
                        kernel32.CloseHandle(h_process)
                        print(f"{ProcessPath} (PID: {pid}) Executed")
                    else:
                        print(f"{ProcessPath} (PID: {pid}) Can`t Executed")
                    

        
