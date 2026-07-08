from src.system import get_os_name, get_kernel, is_steam_installed, is_gamemode_installed

def print_banner():
    print("============================")
    print("      Rogue Forge")
    print("        rfetch")
    print("============================")
    print()


def main():
    print_banner()

    print(f"OS      : {get_os_name()}")
    print(f"Kernel  : {get_kernel()}")

    steam = "Installed ✅" if is_steam_installed() else "Not Installed ❌"

    print(f"Steam   : {steam}")

    gamemode = "Installed ✅" if is_gamemode_installed() else "Not Installed ❌"

    print(f"GameMode : {gamemode}")
if __name__ == "__main__":
    main()
