import platform
import shutil
import subprocess

def get_os_name():
    with open("/etc/os-release", "r") as file:
        for line in file:
            if line.startswith("PRETTY_NAME="):
                return line.split("=", 1)[1].strip().strip('"')

    return "Unknown Linux"


def get_kernel():
    return platform.release()

def is_steam_installed():
    return shutil.which("steam") is not None

def is_gamemode_installed():
    return shutil.which("gamemoderun") is not None

def get_cpu_name():
    with open("/proc/cpuinfo", "r") as file:
        for line in file:
            if line.startswith("model name"):
                return line.split(":", 1)[1].strip().strip('"')            
    return "Unknown CPU"

def get_ram_size():
    with open("/proc/meminfo", "r") as file:
        for line in file:
            if line.startswith("MemTotal"):
                value = line.split(":", 1)[1].strip()
                kb = int(value.split()[0])
                gb = kb/1024/1024
                ram_gb = round(gb, 1)
                return f"{ram_gb} GB"
    return "Unknown RAM"

def get_gpu_name():
    result = subprocess.run(
    ["lspci"],
    capture_output=True,
    text=True
)
    for line in result.stdout.splitlines():
        if "VGA" in line:
            gpu = line.split("VGA compatible controller:")[1]
            gpu = gpu.split("(rev")[0]
            gpu = gpu.strip()   
            return gpu
    return "Unknown GPU"