# Composite File System Simulator

This project is a command-line file system simulator built using the Composite design pattern in Python. It allows users to navigate a virtual directory structure, list files and directories, and count files at various levels of the directory hierarchy.

## Project Overview

The file system simulator includes commands for:
- Navigating through directories (`chdir`, `up`)
- Listing files and subdirectories (`list`, `listall`)
- Counting files in the current directory or all subdirectories (`count`, `countall`)

Where the Composite design pattern primarily comes into play is with our `File` and `Directory` subclasses which both implement and are treated as `Entry` types. This allows uniform handling of files and directories in operations like listing and counting, which makes it easy to extend or modify.

## Key Features

1. **Directory Traversal**: Users can navigate between directories with commands like `chdir` and `up`, simulating a real file system's folder navigation.
2. **Listing and Counting**: Users can list files and directories in the current directory or recursively in all subdirectories. The count commands (`count`, `countall`) provide a quick way to determine the number of files in any directory level.
3. **Composite Pattern**: By using the Composite pattern, `File` and `Directory` objects are treated uniformly as entries, allowing flexible directory operations that work on both types without needing to check the entry type explicitly.

## Usage

To run the program, execute the following command in your terminal in the program directory:

```bash
python3 composite.py
```

Functions that can be passed into command line after the program is run:
- `chdir <directory>`: Change the current directory to the specified directory (`..` for parent directory).
- `up`: Move up one level in the directory hierarchy.
- `list`: List files and directories in the current directory.
- `listall`: List all files and directories recursively in the current directory and below.
- `count`: Count the number of files in the current directory.
- `countall`: Count the number of files recursively in the current directory and below.

## Purpose and Lessons Learned

Through this project, I gained practical experience with the Composite design pattern and saw firsthand how it simplifies working with complex, hierarchical structures like a file system. Implementing `File` and `Directory` classes as shared components under a single `Entry` interface taught me how the Composite pattern allows for uniform handling of individual items and collections. This approach let me build flexible commands for listing and counting that work seamlessly across files and directories without needing to differentiate between them.

Working on this project helped me understand how the Composite pattern can keep code organized and scalable, especially in systems that mimic real-world structures. It highlighted for me the benefits of clean, extendable code and deepened my understanding of design patterns’ role in creating maintainable software. Overall, applying Composite here made the project feel both natural and effective, showing me how design patterns can truly elevate a design.
