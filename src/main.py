from organizer import organize_directory


def main():
    print("=== Smart File Organizer ===")

    directory_path = input("Enter the folder path you want to organize: ")

    organize_directory(directory_path)


if __name__ == "__main__":
    main()