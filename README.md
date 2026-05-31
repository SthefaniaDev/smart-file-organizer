# Smart File Organizer

Smart File Organizer is a Python automation tool that organizes files from a selected folder by category and extension.

The project was created to practice Python automation, file manipulation, project organization, and clean code structure.

## Features

- Organizes files by category
- Creates category folders automatically
- Moves files based on their extensions
- Prevents overwriting files with the same name
- Handles invalid folder paths
- Displays a summary in the terminal
- Uses only Python standard libraries in version 1.0.0

## Supported Categories

The current version supports the following categories:

- Documents
- Images
- Videos
- Audios
- Compressed
- Code
- Executables
- Others

Files with unknown extensions are moved to the `Others` folder.

## Technologies Used

- Python
- pathlib
- shutil
- Git
- GitHub

## Project Structure

```text
smart-file-organizer/
│
├── src/
│   ├── main.py
│   ├── organizer.py
│   └── categories.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

Follow the steps below to run the project on your machine.

### 1. Clone the repository

```bash
git clone https://github.com/SthefaniaDev/smart-file-organizer.git
```

### 2. Access the project folder

```bash
cd smart-file-organizer
```

### 3. Create a virtual environment

On Windows:

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

On Windows PowerShell:

```bash
.venv\Scripts\Activate
```

If PowerShell blocks the activation, run:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate again:

```bash
.venv\Scripts\Activate
```

### 5. Install dependencies

Version 1.0.0 does not require external libraries.

However, if a `requirements.txt` file exists, you can run:

```bash
pip install -r requirements.txt
```

### 6. Run the project

```bash
python src/main.py
```

### 7. Enter the folder path

When the program asks for the folder path, type the path of the folder you want to organize.

Example:

```text
C:\Users\User\Desktop\material
```

The program will organize the files into folders such as:

```text
Documents/
Images/
Videos/
Audios/
Compressed/
Code/
Executables/
Others/
```

## Example Output

```text
=== Smart File Organizer ===

Enter the folder path you want to organize: C:\Users\User\Desktop\material

Moved: report.pdf -> Documents/
Moved: photo.png -> Images/
Moved: music.mp3 -> Audios/
Moved: script.py -> Code/
Moved: installer.exe -> Executables/

Organization completed. 5 file(s) moved.
```

## Version

Current version:

```text
v1.0.0
```

## Author

Developed by Sthefania Ferreira.

- LinkedIn: https://www.linkedin.com/in/sthefania-ferreira
- GitHub: https://github.com/SthefaniaDev
