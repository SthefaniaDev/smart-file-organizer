from pathlib import Path
import shutil

from categories import CATEGORIES


def get_category(extension):

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination_path):

    """
    Generates a unique file path to avoid overwriting existing files.
    If the file already exists, adds a number to the file name.
    """

    destination_path = Path(destination_path)

    if not destination_path.exists():
        return destination_path

    counter = 1
    directory = destination_path.parent
    filename = destination_path.stem
    extension = destination_path.suffix

    while True:
        new_path = directory / f"{filename}_{counter}{extension}"

        if not new_path.exists():
            return new_path

        counter += 1


def organize_directory(directory_path):

    directory = Path(directory_path)

    if not directory.exists():
        print("Error: the specified folder does not exist.")
        return

    if not directory.is_dir():
        print("Error: the specified path is not a folder.")
        return

    moved_files = 0

    for file in directory.iterdir():
        if file.is_file():
            try:
                extension = file.suffix.lower()
                category = get_category(extension)

                category_folder = directory / category
                category_folder.mkdir(exist_ok=True)

                destination_path = category_folder / file.name
                destination_path = get_unique_path(destination_path)

                shutil.move(str(file), str(destination_path))

                print(f"Moved: {file.name} -> {category}/")
                moved_files += 1

            except PermissionError:
                print(f"Permission denied: {file.name}")

            except FileNotFoundError:
                print(f"File not found: {file.name}")

            except Exception as error:
                print(f"Error moving {file.name}: {error}")

    print(f"\nOrganization completed. {moved_files} file(s) moved.")