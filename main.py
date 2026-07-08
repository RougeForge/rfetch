from src.system import get_os_name, get_kernel


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


if __name__ == "__main__":
    main()
