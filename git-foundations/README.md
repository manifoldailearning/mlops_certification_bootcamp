# Git Foundations

This README contains basic Git commands and configurations for reference.

## Command Line Basics

### File System Navigation
- `pwd` - Print Working Directory: Shows the current directory path
- `ls` - List: Shows visible files and directories in current directory
- `ls -a` - List All: Shows both hidden and visible files and directories
- `cd <path_to_directory>` - Change Directory: Navigate to specified directory
- `cd ..` - Change Directory Up: Navigate to parent directory
- `mkdir <directory_name>` - Make Directory: Create a new directory/folder

## Git Commands

### Basic Git Commands
- `git commit -m "message"` - Commit changes with a message
  - Note: Use single dash (-) or double dash (--) for command options

## Git Configuration

### View Configuration
- `git config --global --list` - List all global Git configurations

### Set User Configuration
- `git config --global user.name "your_name"` - Set global Git username
- `git config --global user.email "your_email"` - Set global Git email

Example:
```bash
git config --global user.name "nachiketh"
git config --global user.email "murthy@manifoldailearning.in"
```

## Local Repository Operations

### Repository Initialization
- `.git` - Hidden directory that represents a Git repository
- `git init` - Initialize a new Git repository in the current directory

### File Tracking
- `git status` - Check the status of files in the repository
  - Shows untracked, modified, and staged files

### Staging Files
- `git add <filename>` - Stage a single file for commit
- `git add <filename1> <filename2> <filename3>` - Stage multiple files for commit
- `git add .` - Stage all files in the current directory for commit

### Committing Changes
- `git commit -m "<message>"` - Commit staged changes with a descriptive message
- `git log` - View commit history with details like author, date, and commit messages

Example workflow:
```bash
# Initialize a new repository
git init

# Check status of files
git status

# Stage files for commit
git add example.txt
# or
git add file1.txt file2.txt
# or
git add .

# Commit the changes
git commit -m "Initial commit with example files"

# View commit history
git log
```