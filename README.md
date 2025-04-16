# Android Project to Text File Exporter

## Purpose

This Python script exports an entire Android project's source code and configuration files into a single text file. This is particularly useful for:

- Sharing code for review via text-based platforms
- Using the code with AI tools like Claude, GPT, etc.
- Creating a text-based backup of your project's code
- Submitting code for academic assignments
- Making your codebase searchable in a single document

The script intelligently filters out binary files, build artifacts, and other non-essential files to produce a clean, readable text document containing all your project's code.

## Features

- Exports all source code files (.java, .kt, .xml, etc.) into a single document
- Preserves file paths and directory structure in comments
- Automatically skips binary files, build folders, and other non-source content
- Adds clear headers between files for better readability
- Handles Unicode content correctly
- Works on Windows, macOS, and Linux

## Requirements

- Python 3.6 or higher

## Usage

1. **Download** the script to your computer
2. **Edit** the `project_dir` variable at the top of the script to point to your Android project:

```python
# Example paths:
# Windows: r"C:\Users\YourName\AndroidStudioProjects\YourProject"
# macOS/Linux: "/Users/YourName/AndroidStudioProjects/YourProject" 
project_dir = r"C:\path\to\your\android\project"  # CHANGE THIS!
```

3. **Run** the script:

```
python android_project_to_txt.py
```

4. **Find** the output file (`android_project_export.txt`) in the same directory where you ran the script

## Customization

You can customize the script by modifying:

- **Output file name**: Change the `output_file` variable
- **Directories to skip**: Add or remove entries in the `skip_dirs` list
- **File types to skip**: Add or remove extensions in the `skip_extensions` list 

## Output Format

The exported text file has the following format:

```
ANDROID PROJECT EXPORT
====================
Project: YourProjectName
Date: YYYY-MM-DD HH:MM:SS
====================


# FILE: MainActivity.java
# -------------------------------------
# PATH: app/src/main/java/com/example/yourapp/MainActivity.java
# TYPE: java
# -------------------------------------

[File content appears here]

# END OF FILE: MainActivity.java


# FILE: activity_main.xml
# -------------------------------------
# PATH: app/src/main/res/layout/activity_main.xml
# TYPE: xml
# -------------------------------------

[File content appears here]

# END OF FILE: activity_main.xml

[And so on for all files in the project]
```

## Troubleshooting

- **Unicode errors with Windows paths**: Make sure to use a raw string (`r"..."`) for the path or use forward slashes instead of backslashes
- **Memory errors with large projects**: Try to exclude more directories or file types
- **File not found errors**: Verify the project path is correct and the script has permission to access it

## License

This script is provided as-is, free for personal and commercial use.

## Contributing

Feel free to improve this script and share your modifications!
