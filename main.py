from src.system import get_os_name


def print_banner():
    print("============================")
    print("      Rogue Forge")
    print("        rfetch")
    print("============================")
    print()


def main():
    print_banner()

    print(f"OS : {get_os_name()}")


if __name__ == "__main__":
    main()
