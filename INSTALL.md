# Installation and Running Guide

## System Requirements

- **Python**: 3.8 or higher
- **OS**: Windows, macOS, or Linux
- **RAM**: 512 MB minimum
- **Storage**: 100 MB for application and dependencies

## Installation Steps

### Step 1: Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd finance-tracker

# Or download the ZIP file and extract it
cd finance-tracker
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
# Windows
python src/main.py

# macOS/Linux
python3 src/main.py
```

## Troubleshooting

### Error: "No module named 'matplotlib'"
**Solution**: Install missing package
```bash
pip install matplotlib
```

### Error: "No module named 'tkcalendar'"
**Solution**: Install missing package
```bash
pip install tkcalendar
```

### Error: "tkinter not found"
**Solution**: Install tkinter
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS (usually included with Python.org installer)
# Or install via homebrew:
brew install python-tk@3.12
```

### Error: "sqlite3 not found"
**Note**: sqlite3 is built-in with Python, so this usually shouldn't occur.
If it does, you may need to reinstall Python.

## Verification

After installation, verify everything is working:

```bash
python -c "
import tkinter
import sqlite3
import matplotlib
import tkcalendar
from PIL import Image
print('All dependencies installed successfully!')
"
```

## First Run

1. The application will create a database file (`finance_tracker.db`) automatically
2. Default categories will be initialized in the database
3. The GUI will open with all tabs available

## Running on Different Platforms

### Windows Command Line
```powershell
python src/main.py
```

### Windows PowerShell
```powershell
& 'path/to/.venv/Scripts/python.exe' src/main.py
```

### macOS Terminal
```bash
python3 src/main.py
```

### Linux Terminal
```bash
python3 src/main.py
```

## Creating a Shortcut (Windows)

Create a `.bat` file named `run.bat` in the project directory:

```batch
@echo off
cd /d %~dp0
python src/main.py
pause
```

Then double-click `run.bat` to run the application.

## Setting Up a Desktop Shortcut (Windows)

1. Right-click on the desktop
2. Select "New" → "Shortcut"
3. Enter the path: `python D:\path\to\finance-tracker\src\main.py`
4. Name it "Personal Finance Tracker"
5. Click "Finish"

## Running in Development Mode

If you want to make code changes:

1. Edit the Python files
2. Save the changes
3. Restart the application

The application uses SQLite, so your data will persist between sessions.

## Updating Dependencies

To update to the latest versions of dependencies:

```bash
pip install --upgrade -r requirements.txt
```

## Uninstalling

To remove the application and dependencies:

```bash
# Deactivate virtual environment (if using one)
deactivate

# Remove the project folder
# Windows
rmdir /s finance-tracker

# macOS/Linux
rm -rf finance-tracker
```

## Performance Tips

1. **Keep database clean**: Regularly review old transactions
2. **Use specific date ranges**: Filter data to improve performance
3. **Archive old data**: Export and backup older transactions periodically
4. **Monitor disk space**: Ensure adequate storage for database growth

## Data Backup

To backup your data:

```bash
# Windows
copy finance_tracker.db finance_tracker_backup.db

# macOS/Linux
cp finance_tracker.db finance_tracker_backup.db
```

## Getting Help

1. Check the README.md for comprehensive documentation
2. Review FEATURES.md for feature descriptions
3. Check QUICKSTART.md for quick usage tips
4. Review the inline code comments in source files

## System Information

To check your Python version and installed packages:

```bash
# Check Python version
python --version

# List all installed packages
pip list

# Check Python installation location
python -c "import sys; print(sys.executable)"
```
