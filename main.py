from src.system import get_os_name, get_kernel, is_steam_installed, is_gamemode_installed, get_cpu_name, get_ram_size, get_gpu_name, get_disk_usage, get_uptime, get_desktop_environment, get_display_server, get_shell, get_architecture, get_host

def print_banner():
    print("============================")
    print("      Rogue Forge")
    print("        rfetch")
    print("============================")
    print()


def main():
    print_banner()

    print(f"{"OS":<13}: {get_os_name()}")
    print(f"{"Kernel":<13}: {get_kernel()}")
    print(f"{"CPU":<13}: {get_cpu_name()}")
    print(f"{"RAM":<13}: {get_ram_size()}")
    print(f"{"GPU":<13}: {get_gpu_name()}")
    total, used, free = get_disk_usage()
    print(f"{"Disk":<13}: {used} GB / {total} GB ({free} GB free)")
    steam = "Installed ✅" if is_steam_installed() else "Not Installed ❌"

    print(f"{"Steam":<13}: {steam}")
    hours, mins = get_uptime()
    print(f"{"UpTime":<13}: {hours}h {mins}m")
    print(f"{"Desktop":<13}: {get_desktop_environment()}")
    print(f"{"Display":<13}: {get_display_server()}")
    print(f"{"Shell":<13}: {get_shell()}")
    print(f"{"Architecture":<13}: {get_architecture()}")
    print(f"{'Host':<13}: {get_host()}")
    gamemode = "Installed ✅" if is_gamemode_installed() else "Not Installed ❌"

    print(f"{"GameMode":<13}: {gamemode}")

if __name__ == "__main__":
    main()
