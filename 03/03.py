import sys
from pathlib import Path
from colorama import init, Fore, Style


def list_directory(path: Path, level=0):
    try:
        items = list(path.iterdir())
    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
        return
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
        return
    except PermissionError:
        print(f"Error: Permission denied for accessing '{path}'.")
        return

    directories = [item for item in items if item.is_dir()]
    files = [item for item in items if item.is_file()]

    for directory in directories:
        print("  " * level + Fore.BLUE + f"📂 {directory.name}" + Style.RESET_ALL)
        list_directory(directory, level + 1)

    for file in files:
        print("  " * level + Fore.GREEN + f"📜 {file.name}" + Style.RESET_ALL)

def main():
    if len(sys.argv) != 2:
        print("Usage: python 03.py <path_to_directory>")
        return

    # Ініціалізація colorama
    init(autoreset=True)

    # Отримання шляху до директорії
    path = Path(sys.argv[1])

    # Перевірка, чи існує шлях
    if not path.exists():
        print(f"Error: The path '{path}' does not exist.")
        return

    # Перевірка, чи є шлях директорією
    if not path.is_dir():
        print(f"Error: The path '{path}' is not a directory.")
        return

    # Виведення структури директорії
    list_directory(path)

if __name__ == "__main__":
    main()
