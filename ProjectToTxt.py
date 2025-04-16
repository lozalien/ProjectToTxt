#!/usr/bin/env python3
"""
Android Project to Text File Exporter

This script exports an Android project's source code and configuration files
into a single text file for easy sharing, code review, or AI tool usage.

Usage:
1. Update the project_dir variable with your Android project path
2. Run the script: python android_project_to_txt.py
3. Find the output in android_project_export.txt
"""

import os
import sys
from datetime import datetime

# =====================================================================
# CONFIGURATION - CHANGE THIS PART
# =====================================================================

# Path to your Android project
# Use one of these formats:
# 1. Raw string: r"C:\path\to\your\project"
# 2. Forward slashes: "C:/path/to/your/project"
# 3. Escaped backslashes: "C:\\path\\to\\your\\project"
project_dir = r"C:\path\to\your\android\project"  # CHANGE THIS!

# Output file name
output_file = "android_project_export.txt"

# =====================================================================
# Skip patterns - adjust if needed
# =====================================================================
skip_dirs = [
    "build", ".gradle", ".idea", ".git", "node_modules",
    "generated", "tmp", "temp", "captures", ".cxx"
]

skip_extensions = [
    # Images
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".svg", ".tiff",
    # Binaries
    ".jar", ".aar", ".so", ".dll", ".exe", ".apk", ".aab", ".dex",
    # Compressed files
    ".zip", ".rar", ".7z", ".gz", ".tar",
    # Other large/binary files
    ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx"
]

# =====================================================================
# Script logic - no need to modify below this line
# =====================================================================

def should_skip(path):
    """Check if a path should be skipped"""
    # Skip directories in the exclude list
    norm_path = path.replace("\\", "/")
    for skip_dir in skip_dirs:
        if f"/{skip_dir}/" in norm_path or norm_path.endswith(f"/{skip_dir}"):
            return True
    
    # Skip files with extensions in the exclude list
    _, ext = os.path.splitext(path.lower())
    if ext in skip_extensions:
        return True
    
    # Skip very large files (> 1MB)
    try:
        if os.path.isfile(path) and os.path.getsize(path) > 1024 * 1024:
            return True
    except:
        pass
    
    return False

def process_directory(directory, output):
    """Process all files in the directory and its subdirectories"""
    for root, dirs, files in os.walk(directory):
        # Skip certain directories
        if should_skip(root):
            continue
        
        # Process files in this directory
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip certain files
            if should_skip(file_path):
                continue
            
            # Get relative path from project root
            rel_path = os.path.relpath(file_path, directory)
            
            # Write file header
            output.write("\n\n")
            output.write(f"# FILE: {file}\n")
            output.write("# -------------------------------------\n")
            output.write(f"# PATH: {rel_path}\n")
            ext = os.path.splitext(file)[1][1:] if os.path.splitext(file)[1] else "no_extension"  # Get extension without the dot
            output.write(f"# TYPE: {ext}\n")
            output.write("# -------------------------------------\n\n")
            
            # Try to read file content
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    output.write(content)
            except UnicodeDecodeError:
                output.write("# [Binary file content not shown]\n")
            except Exception as e:
                output.write(f"# [Error reading file: {str(e)}]\n")
            
            output.write("\n")
            output.write(f"# END OF FILE: {file}\n")

def main():
    try:
        # Validate project directory
        if not os.path.isdir(project_dir):
            print(f"Error: Project directory not found: {project_dir}")
            print("Please update the project_dir variable with your actual project path.")
            sys.exit(1)
            
        print(f"Starting export from: {project_dir}")
        with open(output_file, 'w', encoding='utf-8') as output:
            # Write header
            output.write("ANDROID PROJECT EXPORT\n")
            output.write("====================\n")
            output.write(f"Project: {os.path.basename(os.path.abspath(project_dir))}\n")
            output.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            output.write("====================\n\n")
            
            # Process all files
            process_directory(project_dir, output)
            
        print(f"Export completed to {output_file}")
        print(f"File size: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()